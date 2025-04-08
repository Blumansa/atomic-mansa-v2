from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)

class Signal(Base):
    __tablename__ = "signals"

    id = Column(Integer, primary_key=True, index=True)
    pair = Column(String, nullable=False)
    entry = Column(String, nullable=False)
    sl = Column(String, nullable=False)
    tp = Column(String, nullable=False)
    rr = Column(String, nullable=False)
    probability = Column(String)
    status = Column(String)
    cot_alignment = Column(String)
    badge = Column(String)
    pdf_url = Column(String)
