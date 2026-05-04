# FastAPI User and Task Manager
A REST API built with FastAPI and PostgreSQL featuring two related models - Users and Tasks
## Features
- create and manage users
- create and manage tasks linked to users
- Automatic task status tracking (on process/ done)
- PostgreSQL database with SQLALchemy ORM
- Pydantic validation
## Tech Stack
-FastAPI
- PostgreSQL
- SQLALchemy
- Python 3.14
## Endpoints
### Users
-POST /users - create user
-GET /users - get all users
### Tasks
-POST /tasks - create task
-GET /tasks - get all tasks
-GET / users/{task_id}/tasks - get tasks by user
-PUT / tasks/{task_id} - update task
-DELETE /tasks/{task_id} - delete task
