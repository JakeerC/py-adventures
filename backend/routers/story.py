import uuid
from typing import Optional
from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException, Cookie, Response, BackgroundTasks
from sqlalchemy.orm import Session

from db.database import get_db, SessionLocal
from models.story import Story, StoryNode
from models.job import StoryJob

from schemas.story import (
    CompleteStoryNodeResponse,
    CreateStoryRequest,
    CompleteStoryResponse,
)

from schemas.job import StoryJobResponse
from core.story_generator import StoryGenerator

router = APIRouter(prefix="/stories", tags=["stories"])


def get_session_id(session_id: Optional[str] = Cookie(None)):
    # if session_id is None:
    #     raise HTTPException(status_code=401, detail="Session ID not found")
    if session_id is None:
        session_id = str(uuid.uuid4())
    return session_id


@router.post("/create", response_model=StoryJobResponse)
def create_story(
    request: CreateStoryRequest,
    response: Response,
    background_tasks: BackgroundTasks,
    session_id: str = Depends(get_session_id),
    db: Session = Depends(get_db),
) -> StoryJobResponse:
    """Create a new story generation job based on the provided theme"""
    response.set_cookie(key="session_id", value=session_id, httponly=True)
    job_id = str(uuid.uuid4())
    job = StoryJob(
        job_id=job_id, status="pending", theme=request.theme, session_id=session_id
    )
    db.add(job)
    db.commit()
    # db.refresh(job)
    # TODO: Add background task to generate story
    background_tasks.add_task(
        generate_story_task, job_id=job_id, theme=request.theme, session_id=session_id
    )
    return job


def generate_story_task(job_id: str, theme: str, session_id: str):
    """Background task to generate a story based on the theme"""
    db = SessionLocal()
    try:
        job = db.query(StoryJob).filter(StoryJob.job_id == job_id).first()
        if not job:
            return
        try:
            job.status = "in_progress"
            db.commit()

            # Generate story using the StoryGenerator
            story = StoryGenerator.generate_story(db, session_id, theme)

            job.story_id = str(story.id)
            job.status = "completed"
            job.completed_at = datetime.now()
            db.commit()
        except Exception as e:
            job.status = "failed"
            job.completed_at = datetime.now()
            job.error_message = str(e)
            db.commit()

    finally:
        db.close()


@router.get("/{story_id}/complete", response_model=CompleteStoryResponse)
def get_complete_story(
    story_id: int, db: Session = Depends(get_db)
) -> CompleteStoryResponse:
    story = db.query(Story).filter(Story.id == story_id).first()
    if not story:
        raise HTTPException(status_code=404, detail="Story not found")
    complete_story = build_complete_story_tree(db, story)

    return complete_story


def build_complete_story_tree(db: Session, story: Story) -> CompleteStoryResponse:
    nodes = db.query(StoryNode).filter(StoryNode.story_id == story.id).all()

    node_dict = {}
    for node in nodes:
        node_response = CompleteStoryNodeResponse(
            id=node.id,
            content=node.content,
            is_ending=node.is_ending,
            is_winning_ending=node.is_winning_ending,
            options=node.options,
        )
        node_dict[node.id] = node_response

    root_node = next((node for node in nodes if node.is_root), None)
    if not root_node:
        raise HTTPException(status_code=500, default="Story root node not found")

    return CompleteStoryResponse(
        id=story.id,
        title=story.title,
        session_id=story.session_id,
        created_at=story.created_at,
        root_node=node_dict[root_node.id],
        all_nodes=node_dict,
    )
