from fastapi import APIRouter
from fastapi.responses import FileResponse
from fastapi.exceptions import HTTPException

from app.data.config import RESOURCES_PATH
from app.base.db import get_path_by_uuid

download_router = APIRouter()

@download_router.get('/cloud/download/{uuid}')
async def download_file(uuid: str):

    path = await get_path_by_uuid(uuid)

    if path:

        return FileResponse(path)
    
    raise HTTPException(status_code=422, detail='Internal server error')

