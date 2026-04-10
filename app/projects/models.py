import uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.extensions.database import db
from sqlalchemy import UUID, Column, ForeignKey

# merging table for Project and Tag
project_tag = db.Table("project_tag", 
    Column("project_id", ForeignKey("project.id"), primary_key=True),
    Column("tag_id", ForeignKey("tag.id"), primary_key=True)
)

class Project(db.Model):
    id: Mapped[uuid.UUID] = mapped_column(default=uuid.uuid4, primary_key=True)
    slug: Mapped[str] = mapped_column(unique=True)
    title: Mapped[str] = mapped_column(unique=True)
    description: Mapped[str]
    tags: Mapped[list["Tag"]] = relationship(secondary=project_tag, back_populates="projects")
    link: Mapped[str]
    year: Mapped[int]
    picture_url: Mapped[str] = mapped_column(nullable=True)

    def __repr__(self) -> str:
        return f"<Project {self.title}>"

# n to n relationship between tags and Projects

class Tag(db.Model):
    id: Mapped[uuid.UUID] = mapped_column(default=uuid.uuid4, primary_key=True)
    tag: Mapped[str] = mapped_column(unique=True)
    projects: Mapped[list["Project"]] = relationship(secondary=project_tag, back_populates="tags")

    def __repr__(self) -> str:
        return f"<Tag {self.tag}>"