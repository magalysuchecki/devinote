from typing import Optional

from sqlmodel import Field, SQLModel


class Note(SQLModel, table=True):
    """Modelo Nota."""

    __tablename__ = "note_note"
    id: int | None = Field(default=None, primary_key=True)
    title: str
    content: str = ""
    color: Optional[str] = None
    owner_id: int = Field(foreign_key="user_user.id", index=True)


# dtos


class NoteCreate(SQLModel):
    """Modelo para crear nota."""

    title: str
    content: str = ""
    color: Optional[str] = None
    label_ids: Optional[list[int]] = None


class NoteUpdate(SQLModel):
    """Modelo para actualizar nota."""

    title: Optional[str] = None
    content: Optional[str] = None
    color: Optional[str] = None
    label_ids: Optional[list[int]] = None


class NoteRead(SQLModel):
    """Modelo para ver nota."""

    id: int
    title: str
    content: str
    color: Optional[str]
    model_config = {"from_attributes": True}
