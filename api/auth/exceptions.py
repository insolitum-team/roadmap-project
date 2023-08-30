from fastapi import HTTPException, status


class AuthenticateExecption(HTTPException):
    def __init__(self, detail="Incorrect username or password") -> None:
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=detail,
            headers={"WWW-Authenticate": "Bearer"}
        )


class ValidationException(HTTPException):
    def __init__(self, detail='Could not validate credentials'):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=detail,
            headers={'WWW-Authenticate': 'Bearer'}
        )
