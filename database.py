from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://atomic_db_user:QKbwaRluopqLXrxsPSZXX2R33v35VVAK@dpg-cvqhhjbipnbc73ct4bng-a:5432/atomic_db"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
