from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.auth import get_current_user_id
from app.db import get_db
from app.models import Project

router = APIRouter(prefix="/projects", tags=["projects"])


@router.get("/{project_id}")
def get_project(
    project_id: int,
    current_user_id: int = Depends(get_current_user_id),
    db: Session = Depends(get_db),
):
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    return {
        "id": project.id,
        "name": project.name,
        "owner_id": project.owner_id,
        "requested_by": current_user_id,
    }
