from fastapi import APIRouter

from routes.users import user_router
from routes.todos import todos_router


__all__ = ("router",)


router = APIRouter()
router.include_router(router=user_router)
router.include_router(router=todos_router)