from fastapi import FastAPI

from app.routers.download import download_router
from app.routers.upload import upload_router
from app.base.db import create_tables

app = FastAPI()

app.include_router(download_router)
app.include_router(upload_router)

@app.on_event('startup')
async def startup():
    
    await create_tables()
    print('Started')

@app.get('/')
async def main():
    return { 'dsds': 'dsdsd' }
    