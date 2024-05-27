def get_role(role):
    roles = {
        "Admin": 1,
        "Seller": 2,
        "Customer": 3
    }

    return roles.get(role, 3)