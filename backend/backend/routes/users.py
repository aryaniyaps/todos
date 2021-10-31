from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from backend.database import get_session
from backend.schemas.users import UserCreate
from backend.services.users import create_user, user_by_email


user_router = APIRouter(prefix="/users")


@user_router.get("/me", name="users:read-current")
async def read_current_user():
    """
    Get the current user.
    """
    pass


@user_router.patch("/me", name="users:update-current")
async def update_current_user():
    """
    Update the current user.
    """
    pass


@user_router.post("", name="users:create")
async def create_user(data: UserCreate, session: AsyncSession = Depends(get_session)):
    """
    Create a new user.
    """
    user = await user_by_email(session=session, email=data.email)
    if user is not None:
        raise HTTPException(
            status_code=400,
            detail="User with email already exists.",
        )
    user = await create_user(
        ession=session, 
        password=data.password,
        email=data.email, 
    )
    return user
