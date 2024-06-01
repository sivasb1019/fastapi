#IMPORTING MODULES
import os
from dotenv import load_dotenv
load_dotenv(override=True)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# TRACKPAY_DB_PATH
Base = declarative_base()

TRACKPAY_DB_URL = os.getenv("TRACKPAY_DB_PATH")

trackpay_engine = create_engine(TRACKPAY_DB_URL)

SessionLocal1 = sessionmaker(bind=trackpay_engine, expire_on_commit=False)


# MOS_DB_PATH

MOS_DB_URL = os.getenv("MOS_DB_PATH")

mos_engine = create_engine(MOS_DB_URL)

SessionLocal2 = sessionmaker(bind=mos_engine, expire_on_commit=False)