from core.database import Base
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column


class Image(Base):
    __tablename__ = 'images'

    title: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )
    file_path: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )
    resolution: Mapped[str] = mapped_column(
        String,
        nullable=False,
        comment='Like 100x100 format',
    )
    size: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        comment='Size in bytes',
    )
