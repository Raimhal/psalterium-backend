from fastapi import APIRouter
from . import users, security, catalog


router = APIRouter(prefix='/api')
router.include_router(users.router)
router.include_router(catalog.router)
router.include_router(security.router)
