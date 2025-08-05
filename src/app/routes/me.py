from fastapi import APIRouter, Depends
from utils.msentra import msal_auth, UserInfo

router = APIRouter()

@router.get("/", response_model=UserInfo, response_model_exclude_none=True, response_model_by_alias=False)
async def read_me(current_user: UserInfo = Depends(msal_auth.scheme)) -> UserInfo:
    return current_user
