from fastapi import FastAPI

from api.auth.router import router as auth_router
from api.roadmaps.router import router as roadmaps_router
from api.stats.router import router as stats_router


def get_application() -> FastAPI:
    """Function used to get FastAPI application object.

    Returns:
        FastAPI: FastAPI application object
    """
    application = FastAPI(
        title="Roadmaps API",
        description="This is the API for the Roadmaps project."
    )
    application.include_router(auth_router)
    application.include_router(roadmaps_router)
    application.include_router(stats_router)
    return application


app = get_application()
