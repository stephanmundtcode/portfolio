import uuid
from . import routes, models
from sqlalchemy.orm import Mapped, mapped_column
from app.extensions.database import db
from sqlalchemy import UUID

class Project(db.Model):
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    slug: Mapped[str] = mapped_column(unique=True)
    title: Mapped[str] = mapped_column(unique=True)
    description: Mapped[str]
    tags: Mapped[str]
    link: Mapped[str]
    year: Mapped[int]
    picture_url: Mapped[str]
