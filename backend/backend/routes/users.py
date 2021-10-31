from fastapi import APIRouter


user_router = APIRouter(prefix="/users")


@user_router.get("/me")
async def read_current_user():
    """
    Get the current user.
    """
    pass


@user_router.patch("/me")
async def update_current_user():
    """
    Update the current user.
    """
    pass


@user_router.post("")
async def create_user():
    """
    Create a new user.
    """
    pass
