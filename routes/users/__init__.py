from fastapi import APIRouter
from . import users, roles

router = APIRouter()
router.include_router(users.router)
router.include_router(roles.router)
