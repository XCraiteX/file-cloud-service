from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.types import String

class Base(DeclarativeBase):
    pass 

class Files(Base):
    __tablename__ = 'files'

    file_id: Mapped[String] = mapped_column(String, primary_key=True)
    file_path: Mapped[String] = mapped_column(String, unique=True)
