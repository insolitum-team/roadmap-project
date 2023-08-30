from fastapi import APIRouter, Depends

from api.roadmaps.service import RoadmapsService

router = APIRouter(tags=["main functionality"])


@router.get("/category/{category}")
async def get_roadmaps_by_category(
    category: str,
    service: RoadmapsService = Depends(),
):
    """Route that returns all roadmaps by requested category.

    Args:
        category (str): Category of roadmaps to return.

    Returns:
        List[dict]: List of roadmaps.
    """
    return await service.get_roadmaps_by_category(category=category)
