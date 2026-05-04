from fastapi import FastAPI,HTTPException,Depends
from database import engine,Base,get_db
from models import Users,Tasks
from schemas import User,Task,Update_Task,Task_Response,User_response
from sqlalchemy.orm import Session
app = FastAPI()
Base.metadata.create_all(bind=engine)
@app.post("/tasks",response_model=Task_Response)
def create_task(task:Task,db:Session=Depends(get_db)):
    status = "on process" if task.completed == False else "done"
    db_task = Tasks(
       title = task.title,
       completed = task.completed,
       user_id = task.user_id,
       status = status
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task
@app.post("/users",response_model=User_response)
def create_user(user:User,db:Session=Depends(get_db)):
    user_data = Users(
        name = user.name,
        email = user.email
    )
    db.add(user_data)
    db.commit()
    db.refresh(user_data)
    return user_data
@app.get("/users",response_model=list[User_response])
def all_users(db:Session=Depends(get_db)):
    return db.query(Users).all()
@app.get("/tasks",response_model=list[Task_Response])
def all_tasks(db:Session=Depends(get_db)):
    return db.query(Tasks).all()
@app.get("/users/{task_id}/tasks",response_model=User_response)
def get_user(task_id:int,db:Session=Depends(get_db)):
    user = db.query(Tasks).filter(Tasks.id == task_id).first()
    if not user:
        raise HTTPException(status_code = 404,detail="user task not found")
    return user
@app.put("/tasks/{task_id}",response_model=Task_Response) 
def update_task(task_id:int,update:Update_Task,db:Session=Depends(get_db)):
    task = db.query(Tasks).filter(Tasks.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404,detail="task not found")
    if update.title is not None:
        task.title = update.title
    task.status = "on process" if  task.completed == False else "done"
    db.commit()
    db.refresh(task)
    return task
@app.delete("/tasks/{task_id}")
def delete_task(task_id:int,db:Session=Depends(get_db)):
    task = db.query(Tasks).filter(Tasks.id == task_id).first()
    if not task:
        raise HTTPException(status_code = 404,detail="task not found")
    db.delete(task)
    db.commit()
    return {"message":"task deleted"}



