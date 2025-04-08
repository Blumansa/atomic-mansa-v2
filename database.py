from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

# 🧪 Charge les variables d'environnement
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# 🔌 Connexion à la DB
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 🧱 Base de modèle SQLAlchemy
Base = declarative_base()
