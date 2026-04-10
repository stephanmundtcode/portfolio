import uuid
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from app.extensions.database import db

class Contact(db.Model):
    id: Mapped[uuid.UUID] = mapped_column(default=uuid.uuid4, primary_key=True)
    name: Mapped[str]
    email: Mapped[str]
    message: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"<ContactForm {self.name}>"