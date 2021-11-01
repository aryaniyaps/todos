from fastapi import APIRouter


auth_router = APIRouter(prefix="/auth")


@auth_router.post("/login", name="auth:login")
async def login():
    """
    Log the current user in.
    """
    pass


@auth_router.post("/password/forgot", name="auth:forgot-password")
async def forgot_password():
    """
    Request a password reset email.
    """
    pass


@auth_router.post("/password/reset", name="auth:reset-password")
async def reset_password():
    """
    Reset password for the associated user.
    """
    pass
