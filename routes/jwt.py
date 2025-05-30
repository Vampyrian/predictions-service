import jwt
from fastapi import APIRouter, Body
import os

router = APIRouter()

jwt_secret = "secret"
good_jwt = {
    "mediamtx_permissions": [
        {
            "action": "read",
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



@router.post("/jwt/check_good_jwt_post", tags=["jwt token"])
async def good_jwt_post():
    return good_jwt

@router.get("/jwt/check_good_jwt_get", tags=["jwt token"])
async def good_jwt_post():
    return good_jwt

@router.post("/jwt/check_bad_jwt_post", tags=["jwt token"])
async def good_jwt_post():
    return bad_jwt

@router.get("/jwt/check_bad_jwt_get", tags=["jwt token"])
async def good_jwt_post():
    return bad_jwt




# @router.post("/jwt/log_media_mtx", tags=["jwt token"])
# async def log_media_mtx(content: str = Body(...)):
#
#     safe_filename = os.path.basename('log.txt')
#     file_path = os.path.join(safe_filename)
#
#     with open(file_path, 'a') as f:
#         f.write('\n')
#         f.write(content)
#
#
#     return 'ok'
