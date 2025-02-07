from fastapi import APIRouter, Form, UploadFile

from app.data.config import RESOURCES_PATH, HOST_LINK
from app.utils.uuid import generate_uuid
from app.base.db import create_file

upload_router = APIRouter()

@upload_router.post('/cloud/upload')
async def upload_file(file: UploadFile):
    
    ext = file.filename.split('.')[-1]

    uuid = await generate_uuid()
    path = f'{RESOURCES_PATH}{uuid}.{ext}'
    
    with open(path, 'wb') as f:
        f.write(await file.read())

        status = await create_file(uuid, path)

        if status:

            return { 'status': 'OK', 'details': 'File successfully uploaded!', 'uuid': HOST_LINK + '/file/' + uuid }

    return { 'status': 'Error', 'details': 'Internal server error!'}