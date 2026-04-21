from fastapi import FastAPI
from sqlalchemy.orm import Session

from app.db import Base, engine, SessionLocal
from app.models import User, Project
from app.routes.projects import router as projects_router

app = FastAPI(title="RealmShield IDOR Demo")

Base.metadata.create_all(bind=engine)


def seed_data():
    db: Session = SessionLocal()
    try:
        if db.query(User).count() == 0:
            user1 = User(id=1, username="alice")
            user2 = User(id=2, username="bob")
            db.add_all([user1, user2])
            db.commit()

        if db.query(Project).count() == 0:
            project1 = Project(id=1, name="alice-project", owner_id=1)
            project2 = Project(id=2, name="bob-project", owner_id=2)
            db.add_all([project1, project2])
            db.commit()
    finally:
        db.close()


seed_data()
app.include_router(projects_router)


@app.get("/")
def root():
    return {"status": "ok"}