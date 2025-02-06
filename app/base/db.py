from sqlalchemy import select
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker 
import aiosqlite

from app.base.models import *

engine = create_async_engine("sqlite+aiosqlite:///app/data/files.db")
session = async_sessionmaker(engine, class_=AsyncSession)

async def create_table():

    async with engine.begin() as conn:
        conn.run_sync(Base.metadata.create_all)

async def create_file(uuid: str, path: str):

    async with session() as db:
        new_file = Files(file_id=uuid, file_path=path)

    pass