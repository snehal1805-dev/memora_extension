from fastapi import Depends
from sqlalchemy.orm import Session

from app.database.database import get_db

from app.core.security import verify_token

from app.services.auth_service import get_current_user


def current_user(
    user_id: int = Depends(verify_token),
    db: Session = Depends(get_db)
):
    return get_current_user(
        db,
        user_id
    )