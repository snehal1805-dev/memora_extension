from fastapi import APIRouter
from fastapi import Depends

from app.schemas.auth_schema import UserResponse

from app.utils.dependencies import current_user

from app.models.user_model import User

router = APIRouter(
    prefix="/user",
    tags=["User"]
)


@router.get(
    "/me",
    response_model=UserResponse
)
def get_me(
    user: User = Depends(current_user)
):
    return user