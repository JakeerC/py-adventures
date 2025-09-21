# Story Generator Backend

This is a FastAPI backend for generating interactive stories. Users can create story generation jobs and retrieve complete stories with branching nodes and options.

## Features

- **Create Story Job:** Start a new story generation job by providing a theme.
- **Background Processing:** Story generation runs in the background.
- **Retrieve Complete Story:** Get the full story tree, including all nodes and options.
- **Session Management:** Each user is assigned a session ID via cookies.

## API Endpoints

### Create a Story Job

- **POST** `/stories/create`
- **Body:**
  ```json
  {
    "theme": "A magical forest adventure"
  }
  ```
- **Sample Request (curl):**
  ```bash
  curl -X POST "http://localhost:8000/stories/create" \
    -H "Content-Type: application/json" \
    -d '{"theme": "A magical forest adventure"}' \
    -c cookies.txt
  ```
- **Response Example:**
  ```json
  {
    "job_id": "123e4567-e89b-12d3-a456-426614174000",
    "status": "pending",
    "theme": "A magical forest adventure",
    "session_id": "abcdef12-3456-7890-abcd-ef1234567890"
  }
  ```

### Get Complete Story

- **GET** `/stories/{story_id}/complete`
- **Sample Request (curl):**
  ```bash
  curl -X GET "http://localhost:8000/stories/1/complete" \
    -b cookies.txt
  ```
- **Response Example:**
  ```json
  {
    "id": 1,
    "title": "A Magical Forest Adventure",
    "session_id": "abcdef12-3456-7890-abcd-ef1234567890",
    "created_at": "2024-06-01T12:00:00",
    "root_node": {
      "id": 10,
      "content": "You enter a magical forest...",
      "is_ending": false,
      "is_winning_ending": false,
      "options": [
        { "text": "Go left", "node_id": 11 },
        { "text": "Go right", "node_id": 12 }
      ]
    },
    "all_nodes": {
      "10": {
        /* node data */
      },
      "11": {
        /* node data */
      },
      "12": {
        /* node data */
      }
    }
  }
  ```

## How It Works

1. **Submit a theme** to create a story job.
2. **Background task** generates the story.
3. **Retrieve the story** using the story ID once the job is complete.

## Project Structure

- `routers/story.py` - API endpoints and background tasks.
- `schemas/story.py` - Pydantic models for request and response validation.
- `models/` - Database models.
- `db/` - Database connection and session management.

## Requirements

- Python 3.8+
- FastAPI
- SQLAlchemy
- Pydantic

## Running the Server

1. Install dependencies:
   ```bash
   uv sync
   ```
2. Start the server:
   ```bash
   uv run main.py
   ```
