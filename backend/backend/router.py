from fastapi import APIRouter

from backend.routes.users import user_router
from backend.routes.todos import todos_router


__all__ = ("router",)


router = APIRouter()
router.include_router(router=user_router)
router.include_router(router=todos_router)