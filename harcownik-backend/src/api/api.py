from fastapi import APIRouter
from src.api.endpoints import (badge_reports, badges, groups, level_reports,
                               login, reports_history, users)

api_router = APIRouter()
api_router.include_router(reports_history.router, tags=["reports_history"])
api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, tags=["users"])
api_router.include_router(groups.router, tags=["groups"])
api_router.include_router(badges.router, tags=["badges"])
api_router.include_router(badge_reports.router, tags=["badge_reports"])
api_router.include_router(level_reports.router, tags=["level_reports"])
