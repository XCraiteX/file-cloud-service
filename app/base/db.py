from sqlalchemy import select
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker 
import aiosqlite

from app.base.models import *

engine = create_async_engine("sqlite+aiosqlite:///app/data/files.db")
session = async_sessionmaker(engine, class_=AsyncSession)

async def create_tables():

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def create_file(uuid: str, path: str):

    async with session() as db:
        new_file = Files(file_id=uuid, file_path=path)
        db.add(new_file)

        await db.commit()

        return True
    
    return False


async def get_path_by_uuid(uuid: str):

    async with session() as db:
        result = await db.execute(select(Files).filter(Files.file_id == uuid))
        obj = result.scalars().first()

        if obj:
            return obj.file_path
        
    return False