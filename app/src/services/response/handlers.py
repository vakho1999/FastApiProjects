from typing import Callable, Any, Union

from fastapi import  HTTPException, Header
from starlette.requests import Request
from starlette.responses import JSONResponse, Response

from app.src.schemas.response.enums.types import HttpStatusCodes
from jose import jwt



async def AuthorizationHandler(Authorization: str = Header()):
    """
    Extract the access token from the Authorization header
    """
    auth = Authorization
    if auth:
        parts = auth.split()
        if len(parts) == 2:
            if parts[0].lower() == "bearer":
                try:
                    return jwt.get_unverified_claims(parts[1])["sub"]
                except jwt.ExpiredSignatureError:

                    raise HTTPException(status_code=HttpStatusCodes.UNAUTHORIZED, detail="Signature Expired")
    raise HTTPException(status_code=HttpStatusCodes.UNAUTHORIZED, detail="Not a valid token")



def ResponseHandler(code: HttpStatusCodes) -> Callable[
    [Any], Callable[[Any, tuple[Any, ...], dict[str, Any]], Union[JSONResponse, Any]]]:
    def decorator(f):
        def wrapper(self, *arg, **kwargs):
            status = Response()
            func = None
            try:
                status.status_code = code.value
                status.content = code.name
                func = f(self, *arg, **kwargs)

            except Exception as e:
                import traceback
                print(traceback.format_exc())
                status.status_code = HttpStatusCodes.PROGRAMMING_ERROR.value
                status.content = HttpStatusCodes.PROGRAMMING_ERROR.name

            finally:
                if func:
                    return func
                return JSONResponse(status_code=status.status_code, content=status.content)

        return wrapper

    return decorator
