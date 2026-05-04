from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
data_url = "postgresql://postgres:postgre123@localhost:5432/user-and-task-manager"
engine = create_engine(data_url)
SessionLocal = sessionmaker(autocommit=False,bind=engine)
Base = declarative_base()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

