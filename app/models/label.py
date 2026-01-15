from pydantic import Field
from sqlalchemy import UniqueConstraint
from sqlmodel import SQLModel


class Label(SQLModel, table=True):
    """Modelo Etiqueta."""

    # __tablename__ = "label"
    __table_args__ = [
        UniqueConstraint("owner_id", "name", name="uq_label_owner_name")
    ]

    id: int = Field(default=None, primary_key=True)
    name: str = Field(index=True, min_length=1, max_length=50)
    owner_id: int = Field(foreign_key="user.id", index=True)


class NoteLabelLink(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    note_id: int = Field(foreign_key="note.id", index=True)


# dtos


class LabelCreate(SQLModel):
    """Modelo para crear etiqueta."""

    name: str


class LabelRead(SQLModel):
    """Modelo para ver etiqueta."""

    id: int
    name: str
    model_config = {"from_attributes": True}
