from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm

from app.api.dependencies import AUTH_TOKEN_TYPE, DBSession
from app.models.user import UserCreate, UserRead
from app.repositories.user_repository import UserRepository
from app.services.auth_service import AuthService

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post(
    "register", response_model=UserRead, status_code=status.HTTP_201_CREATED
)
def register(payload: UserCreate, db: DBSession):
    return AuthService(UserRepository(db)).register(payload)


@router.post("/login")
def login(email: str, password: str, db: DBSession):
    return {
        "access_token": AuthService(UserRepository(db)).login(email, password),
        "token_type": AUTH_TOKEN_TYPE,
    }


@router.post("/token")
def login_OAuth2(db: DBSession, form: OAuth2PasswordRequestForm = Depends()):  # noqa: B008
    return {
        "access_token": AuthService(UserRepository(db)).login(
            form.username, form.password
        ),
        "token_type": AUTH_TOKEN_TYPE,
    }
