import json
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.auth.router import router as auth_router
from api.users.router import router as user_router
from api.roadmaps.router import router as roadmaps_router
from api.stats.router import router as stats_router
from api.steps.router import router as steps_router
from api.posts.router import router as posts_router
from api.categories.router import router as categories_router
from common.settings import config


def get_application() -> FastAPI:
    """Function used to get FastAPI application object.

    Returns:
        FastAPI: FastAPI application object
    """
    application = FastAPI(
        title="Insolitum Learn",
        description="This is the API for the Insolitum Learn project.",
    )

    # Routers
    application.include_router(auth_router)
    application.include_router(user_router)
    application.include_router(roadmaps_router)
    application.include_router(stats_router)
    application.include_router(categories_router)
    application.include_router(steps_router)
    application.include_router(posts_router)

    # CORS
    origins = config.CORS_ORIGINS
    application.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return application


app = get_application()
