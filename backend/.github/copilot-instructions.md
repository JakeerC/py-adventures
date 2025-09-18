# AI Coding Agent Instructions for py-adventures Backend

## Project Overview

This is a FastAPI-based backend service for generating and managing adventure stories. The project follows a modular architecture with clear separation of concerns.

## Architecture & Structure

- `core/`: Core business logic and configurations
  - `story_generator.py`: Story generation logic
  - `config.py`: Application configurations
  - `prompts.py`: Story generation prompts
- `db/`: Database layer with SQLite implementation
- `models/`: SQLAlchemy ORM models
- `routers/`: FastAPI route handlers
- `schemas/`: Pydantic models for request/response validation

## Key Conventions

1. **Database**:

   - SQLite database (`database.db`) configured via `DATABASE_URL` in `.env`
   - SQLAlchemy ORM for database operations

2. **API Structure**:

   - All routes are modularized in `routers/` directory
   - Each route module corresponds to a specific domain (e.g., `story.py`, `job.py`)
   - Use Pydantic models from `schemas/` for request/response validation

3. **Environment**:
   - Python 3.10 required (specified in `.python-version`)
   - Dependencies managed with `pyproject.toml`

## Development Workflow

1. **Setup**:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -e ".[dev]"
   ```

2. **Running the Server**:
   ```bash
   uvicorn main:app --reload --port 8000
   ```
   or use the `__main__` block in `main.py`

## Integration Points

- CORS enabled for all origins in development (see `main.py`)
- API documentation available at `/docs` (Swagger) and `/redoc`

## Project Status

This appears to be a new project with the basic structure set up. Many core files are currently empty and TODO items (from `README.md`) include:

- Adding Ruff linter
- Setting up Git hooks
- Adding documentation

When contributing, follow the established modular structure and ensure new endpoints are properly routed through the `routers/` directory.
