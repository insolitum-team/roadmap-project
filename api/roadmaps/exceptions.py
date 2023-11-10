from fastapi import HTTPException, status


class RoadmapNotFoundException(HTTPException):
    def __init__(self, detail="Roadmap not found"):
        super().__init__(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=detail,
            headers={"WWW-Authenticate": "Bearer"},
        )
