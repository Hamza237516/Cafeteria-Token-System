from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# We are using SQLite for easy local development. 
# It will create a file named "cafeteria.db" in your folder.
SQLALCHEMY_DATABASE_URL = "sqlite:///./cafeteria.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()