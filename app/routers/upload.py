from fastapi import APIRouter, Form, UploadFile

from app.data.config import RESOURCES_PATH
from app.utils.uuid import generate_uuid

upload_router = APIRouter()

@upload_router.post('/cloud/upload')
async def upload_file(file: UploadFile):
    
    ext = file.filename.split('.')[-1]

    uuid = await generate_uuid()
    
    with open(RESOURCES_PATH + f'{uuid}.{ext}', 'wb') as f:
        f.write(await file.read())

        return { 'status': 'OK', 'details': 'File successfully uploaded!', 'uuid': uuid }

    return { 'status': 'Error', 'details': 'Internal server error!'}