from fastapi import HTTPException, status


class UserNotFoundException(HTTPException):
    def __init__(self, detail="User not found"):
        super().__init__(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=detail,
            headers={"WWW-Authenticate": "Bearer"},
        )
