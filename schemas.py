from pydantic import BaseModel,Field
from typing import Optional
class User(BaseModel):
    name:str
    email:str
class Task(BaseModel):
    title:str
    completed:bool
    user_id:int = Field(gt=0)
class User_response(BaseModel):
    id:int
    name:str
    email:str
    class Config:
        from_attributes = True
class Task_Response(BaseModel):
    id:int
    title:str
    completed:bool
    user_id:int
    status:str
    class Config:
        from_attributes = True
class Update_Task(BaseModel):
    title:Optional[str]= None
    