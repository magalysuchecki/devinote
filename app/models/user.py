from sqlmodel import Field, SQLModel

# Modelos de base de datos


class User(SQLModel, table=True):
    """Modelo Usuario."""

    id: int = Field(default=None, primary_key=True)
    email: str = Field(index=True, unique=True)
    full_name: str = Field(default="")
    hashed_password: str  # no lleva field por que se genera


# Modelos de validación  (DTOs, Data Transfer Object)


class UserCreate(SQLModel):
    """Modelo para crear usuario."""

    email: str
    full_name: str
    password: str


class UserRead(SQLModel):
    """Modelo para ver usuario."""

    id: int
    email: str
    full_name: str
    model_config = {
        "from_attributes": True  # para tratar como modelo y no como diccionario
    }
