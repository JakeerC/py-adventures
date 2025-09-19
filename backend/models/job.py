# SQLAlchemy model representing a background job for story generation
from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
)
from sqlalchemy.sql import func
from db.database import Base


class StoryJob(Base):
    __tablename__ = "story_jobs"

    # Primary key and unique identifier for the job
    id = Column(Integer, primary_key=True, index=True)

    # Unique identifier for the specific job (could be used for tracking)
    job_id = Column(String, index=True)

    # Identifier linking the job to a user session
    session_id = Column(String, index=True)

    # Theme of the story being generated
    theme = Column(String)

    # Current status of the job (e.g., "pending", "in_progress", "completed", "failed")
    status = Column(String)

    # Foreign key linking to the generated story (populated when complete)
    story_id = Column(Integer, nullable=True)

    # Error message if the job fails
    error = Column(String, nullable=True)

    # Timestamp when the job was created
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Timestamp when the job was completed (nullable since it might not be completed yet)
    completed_at = Column(DateTime(timezone=True), nullable=True)
