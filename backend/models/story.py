from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    Boolean,
    JSON,
    ForeignKey,
)
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from db.database import Base


class Story(Base):
    """Represents a story with its nodes and basic metadata"""

    __tablename__ = "stories"

    id = Column(
        Integer, primary_key=True, index=True
    )  # Unique identifier for the story
    title = Column(String, index=True)  # Title of the story
    session_id = Column(
        String, index=True
    )  # Identifier for the session this story belongs to
    created_at = Column(
        DateTime(timezone=True), server_default=func.now()
    )  # Timestamp when story was created

    # Relationship with StoryNode model (one-to-many)
    nodes = relationship("StoryNode", back_populates="story")


class StoryNode(Base):
    """Represents a node in the story, containing content and options for branching"""

    __tablename__ = "story_nodes"

    id = Column(Integer, primary_key=True, index=True)  # Unique identifier for the node
    story_id = Column(
        Integer, ForeignKey("stories.id"), index=True
    )  # Foreign key linking to Story
    content = Column(String)  # Text content of the story node
    is_root = Column(Boolean, default=False)  # Whether this node is the starting point
    is_ending = Column(Boolean, default=False)  # Whether this node is a story ending
    is_winning_ending = Column(
        Boolean, default=False
    )  # Whether this is a winning ending
    options = Column(JSON, default=list)  # List of options/choices for the player

    # Relationship with Story model (many-to-one)
    story = relationship("Story", back_populates="nodes")
