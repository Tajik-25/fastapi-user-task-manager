from sqlalchemy import Integer,Boolean,Column,String
from database import Base
class Users(Base):
    __tablename__ = "Users"
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String)
    email = Column(String)
class Tasks(Base):
    __tablename__ = "Tasks"
    id = Column(Integer,primary_key=True,index=True)
    title = Column(String)
    completed = Column(Boolean)
    user_id = Column(Integer)
    status = Column(String)