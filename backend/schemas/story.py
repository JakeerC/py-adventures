from typing import List, Optional, Dict
from datetime import datetime
from pydantic import BaseModel


class StoryNodeBase(BaseModel):
    content: str
    is_ending: bool = False
    is_winning_ending: bool = False


class StoryBase(BaseModel):
    title: str
    session_id: Optional[int] = None

    class Config:
        from_attributes = True


class CreateStoryRequest(BaseModel):
    theme: str


class StoryOptionsSchema(BaseModel):
    text: str
    node_id: Optional[str] = None


class CompleteStoryNodeResponse(StoryNodeBase):
    id: int
    options: List[StoryOptionsSchema] = []


class CompleteStoryResponse(StoryBase):
    """
    Represents a complete story response with all associated nodes.

    Attributes:
        id (int): Unique identifier for the story.
        created_at (datetime): Timestamp when the story was created.
        root_node (CompleteStoryNodeResponse): The starting node of the story.
        all_nodes (Dict[int, CompleteStoryNodeResponse]): Dictionary containing all nodes in the story,
            keyed by their node IDs for easy access.
    """

    id: int
    created_at: datetime
    root_node: CompleteStoryNodeResponse
    all_nodes: Dict[int, CompleteStoryNodeResponse]

    class Config:  # type: ignore
        from_attributes = True
