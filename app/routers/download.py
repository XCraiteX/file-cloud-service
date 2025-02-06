from fastapi import APIRouter
from fastapi.responses import FileResponse

from app.data.config import RESOURCES_PATH

download_router = APIRouter()

@download_router.post('/cloud/download/')
async def download_file(uuid: str):

    return FileResponse(RESOURCES_PATH + uuid)

