from fastapi import APIRouter

from backend.routes.auth import auth_router
from backend.routes.users import user_router
from backend.routes.todos import todo_router


__all__ = ("router",)


router = APIRouter()
router.include_router(router=auth_router)
router.include_router(router=user_router)
router.include_router(router=todo_router)