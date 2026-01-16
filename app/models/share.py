from enum import Enum

from sqlalchemy import UniqueConstraint
from sqlmodel import Field, SQLModel


class ShareRole(str, Enum):
    """Clase de roles."""

    READ = "read"
    EDIT = "edit"


class NoteShare(SQLModel, table=True):
    """Modelo Nota Compartida."""

    __tablename__ = "share_noteshare"
    __table_args = (
        UniqueConstraint("note_id", "user_id", name="uq_note_user"),
    )

    id: int | None = Field(default=None, primary_key=True)
    note_id: int = Field(foreign_key="note_note.id", index=True)
    user_id: int = Field(foreign_key="user_user.id", index=True)
    role: ShareRole = Field(default=ShareRole.READ)


class LabelShare(SQLModel, table=True):
    """Modelo Etiqueta Compartida."""

    __tablename__ = "share_labelshare"
    __table_args = (
        UniqueConstraint("label_id", "user_id", name="uq_label_user"),
    )

    id: int | None = Field(default=None, primary_key=True)
    label_id: int = Field(foreign_key="label_label.id", index=True)
    user_id: int = Field(foreign_key="user_user.id", index=True)
    role: ShareRole = Field(default=ShareRole.READ)


class ShareRequest(SQLModel):
    """Modelo para compartir objetos."""

    target_user_id: int = Field(gt=0)
    role: ShareRole = ShareRole.READ
