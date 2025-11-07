# VembuBDR HelperService Design Documentation

## 1. Architecture Overview

### 1.1 System Architecture
```
┌─────────────────────────────────────────────────────────────┐
│                    VembuBDR Server Process                  │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────────┐    ┌─────────────────────────────────┐ │
│  │ Backup Process  │    │      IPC Communication          │ │
│  │ ┌─────────────┐ │    │ ┌─────────────────────────────┐ │ │
│  │ │ServerObject │ │◄──►│ │SendSpaceValidationRequest   │ │ │
│  │ │Thread       │ │    │ │ProcessSpaceExceedNotify     │ │ │
│  │ │ProcessBackup│ │    │ │RequesterToHelperService     │ │ │
│  │ └─────────────┘ │    │ │HelperServiceToRequester     │ │ │
│  │ ┌─────────────┐ │    │ └─────────────────────────────┘ │ │
│  │ │ResetAction  │ │    │                                 │ │
│  │ │ResetBackup  │ │    │                                 │ │
│  │ │Action       │ │    │                                 │ │
│  │ └─────────────┘ │    │                                 │ │
│  └─────────────────┘    └─────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
                               │
                               │ Named Pipes (Windows)
                               │ Unix Sockets (Linux)
                               │
┌──────────────────────────────────────────────────────────────┐
│                  HelperService Process                       │
├──────────────────────────────────────────────────────────────┤
│  ┌─────────────────────────────────────────────────────────┐ │
│  │                 HelperService Core                      │ │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────────┐  │ │
│  │  │ Singleton   │  │ IPC Handler │  │ Module Registry │  │ │
│  │  │ Management  │  │ Thread      │  │ Template System │  │ │
│  │  │ - Instance  │  │ - Receiver  │  │ - Dynamic Load  │  │ │
│  │  │ - Lifecycle │  │ - Sender    │  │ - Type Safety   │  │ │
│  │  └─────────────┘  └─────────────┘  └─────────────────┘  │ │
│  └─────────────────────────────────────────────────────────┘ │
│                              │                               │
│                              ▼                               │
│  ┌─────────────────────────────────────────────────────────┐ │
│  │              IHelperModule Interface                    │ │
│  │  ┌────────────────────────────────────────────────────┐ │ │
│  │  │ virtual void Initialize() = 0;                     │ │ │
│  │  │ virtual void Shutdown() = 0;                       │ │ │
│  │  │ virtual bool IsActive() const = 0;                 │ │ │
│  │  └────────────────────────────────────────────────────┘ │ │
│  └─────────────────────────────────────────────────────────┘ │
│                              │                               │
│                              ▼                               │
│  ┌─────────────────────────────────────────────────────────┐ │
│  │            SpaceValidationModule                        │ │
│  │  ┌────────────────────────────────────────────────────┐ │ │
│  │  │ Reference Counting: map<int, int>                  │ │ │
│  │  │ - entityID → reference count                       │ │ │
│  │  │ - Thread-safe operations                           │ │ │
│  │  │ - Auto cleanup when count = 0                      │ │ │
│  │  └────────────────────────────────────────────────────┘ │ │
│  │  ┌────────────────────────────────────────────────────┐ │ │
│  │  │ Integration Layer                                  │ │ │
│  │  │ - SpaceValidationThread::SpaceRegisterProcess()    │ │ │
│  │  │ - SpaceValidationThread::SpaceDeRegisterProcess()  │ │ │
│  │  └────────────────────────────────────────────────────┘ │ │
│  └─────────────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────────────┘
```

## 2. Component Design Details

### 2.1 Design Patterns Used
1. **Singleton Pattern**: Ensures single instance per process
2. **Template Method Pattern**: Module registration system
3. **Strategy Pattern**: IHelperModule interface for different modules
4. **RAII Pattern**: Automatic resource management
5. **Observer Pattern**: IPC message handling

## 3. IPC Communication Design

### 3.1 Message Protocol Design

#### Message Format
```
Space Validation Request: "ACTION:accountID:tenantID:globalRepoID:entityType"
- ACTION: "START" or "STOP"
- accountID: Account identifier
- tenantID: Tenant identifier  
- globalRepoID: Repository identifier
- entityType: Entity type enum value
```

### 3.2 Bidirectional Communication

#### Pipe Configuration
```
Requester → HelperService: "RequesterToHelperService"
HelperService → Requester: "HelperServiceToRequester"
```

#### Message Types
```cpp
enum MAction {
    eSpaceValidationRequest = 26,        // Request validation start/stop
    eHelperToRequesterSpaceExceeded,     // Notify space exceeded
    eParentToChildSpaceExceeded          // Legacy child notification
};
```

## 4. Threading Model

### 4.1 Thread Architecture
```
Main Thread:
├── HelperService::Run() - Main event loop
├── Module lifecycle management
└── Auto-shutdown monitoring

IPC Receiver Thread:
├── IPCMsgReceiverThread - Message reception
├── Message parsing and routing
└── Asynchronous message processing

Module Threads:
├── SpaceValidationThread instances
├── Space monitoring operations
└── Independent per entity
```

## 5. Integration Points

### 5.1 VembuBDR Server Integration
```cpp
// StartStoreGridServer.cpp
case SpawnProcessUtil::eHelperService:
    StartHelperService();  // Launch HelperService process
```

### 5.2 Backup Process Integration
```cpp
// ServerObjectThread.cpp - start
void ProcessBackup() {
    if (spawn_enabled) {
        SendSpaceValidationRequestToHelperService(...);
    }
}

// ResetAction.cpp - end
void ResetBackupAction() {
    if (spawn_enabled) {
        SendSpaceValidationStopRequestToHelperService(...);
    }
}
```

### 5.3 Space Validation Integration
```cpp
// SpaceValidationModule → SpaceValidationThread
SpaceValidationThread::SpaceRegisterProcess(accountID, tenantID, globalRepoID, entityType);
SpaceValidationThread::SpaceDeRegisterProcess(entityType, entityID, globalRepoID);
```

## 6. Configuration and Deployment

### 6.1 Build Configuration
- **Conditional Compilation**: Spawn process feature flags
- **Platform Support**: Windows and Linux compatibility
- **Module Selection**: Compile-time module inclusion

### 6.2 Runtime Configuration
- **Auto-Start**: Launched automatically when backup starts and spawn enabled
- **IPC Channels**: Named pipes with process-specific names
- **Logging**: Separate log files per module and entity
- **Timeout Settings**: 5-minute inactivity timeout (configurable)

## 7. Future Extensibility

### 7.1 Adding New Modules
```cpp
// 1. Implement IHelperModule interface
class NewModule : public IHelperModule {
    void Initialize() override { /* setup */ }
    void Shutdown() override { /* cleanup */ }
    bool IsActive() const override { /* check activity */ }
};

// 2. Register in HelperService
void RegisterModules() {
    RegisterModule<SpaceValidationModule>("SpaceValidation");
    RegisterModule<NewModule>("NewModule");  // Add this line
}

// 3. Add IPC message handling
case IPCUtil::MAction::eNewModuleRequest:
    HandleNewModuleRequest(backupInfo);
    break;
```

### 7.2 Scalability Enhancements
- **Load Balancing**: Multiple HelperService instances
- **Distributed Processing**: Cross-machine module execution
- **Caching Layer**: Module state persistence
- **Monitoring Integration**: Health checks and metrics
