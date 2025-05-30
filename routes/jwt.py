import jwt
from fastapi import APIRouter

router = APIRouter()

jwt_secret = "secret"
good_jwt = {
    "mediamtx_permissions": [
        {
            "action": "publish",
            "path": ""
        }
    ]
}

bad_jwt = {
    "mediamtx_permissions": [
        {
            "action": "publish1",
            "path": ""
        }
    ]
}

@router.post("/jwt/goog_jwt_post", tags=["jwt token"])
async def good_jwt_post():
    encoded_jwt = jwt.encode(good_jwt, jwt_secret, algorithm="HS256")

    return encoded_jwt

@router.get("/jwt/goog_jwt_get", tags=["jwt token"])
async def good_jwt_post():
    encoded_jwt = jwt.encode(good_jwt, jwt_secret, algorithm="HS256")

    return encoded_jwt

@router.post("/jwt/bad_jwt_post", tags=["jwt token"])
async def good_jwt_post():
    encoded_jwt = jwt.encode(bad_jwt, jwt_secret, algorithm="HS256")

    return encoded_jwt

@router.get("/jwt/bad_jwt_get", tags=["jwt token"])
async def good_jwt_post():
    encoded_jwt = jwt.encode(bad_jwt, jwt_secret, algorithm="HS256")

    return encoded_jwt