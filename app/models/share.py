from pydantic import Field
from sqlalchemy import UniqueConstraint
from sqlmodel import Enum, SQLModel


class ShareRole(str, Enum):
    READ = "read"
    EDIT = "edit"


class NoteShare(SQLModel, table=True):
    __table_args = [UniqueConstraint("note_id", "user_id", name="uq_note_user")]

    id: int = Field(default=None, primary_key=True)
    note_id: int = Field(foreign_key="note.id", index=True)
    user_id: int = Field(foreign_key="user.id", index=True)
    role: ShareRole = Field(default=ShareRole.READ)


class LabelShare(SQLModel, table=True):
    __table_args = [
        UniqueConstraint("label_id", "user_id", name="uq_label_user")
    ]

    id: int = Field(default=None, primary_key=True)
    label_id: int = Field(foreign_key="label.id", index=True)
    user_id: int = Field(foreign_key="user.id", index=True)
    role: ShareRole = Field(default=ShareRole.READ)
