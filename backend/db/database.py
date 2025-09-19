from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from core.config import settings

# Create database engine using the configured DATABASE_URL
engine = create_engine(settings.DATABASE_URL)

# Create a configured "Session" class for database sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for all SQLAlchemy models
Base = declarative_base()


# Dependency to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Create all database tables based on SQLAlchemy models
def create_tables():
    # import models.story  # Import all models here to ensure they are registered
    Base.metadata.create_all(bind=engine)
