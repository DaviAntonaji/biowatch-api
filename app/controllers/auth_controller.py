from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.repositories.auth_repository import AuthRepository
from app.schemas.auth_schema import UserCreate, UserResponse, UserLogin
from app.database import SessionLocal
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from app.config import settings

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        # Decodifica o token
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        print("payload", payload)
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError as e:
        print(f"JWT Error: {str(e)}")  # Debug
        raise credentials_exception

    user = AuthRepository(db).get_user_by_email(email=email)
    if user is None:
        raise credentials_exception
    return user

@router.post("/register", response_model=UserResponse)
def register(user_create: UserCreate, db: Session = Depends(get_db)):
    auth_repo = AuthRepository(db)
    db_user = auth_repo.get_user_by_email(email=user_create.email)
    if db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
    return auth_repo.create_user(user_create)

@router.post("/login")
def login(form_data: UserLogin, db: Session = Depends(get_db)):
    auth_repo = AuthRepository(db)
    user = auth_repo.authenticate_user(email=form_data.email, password=form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    access_token = auth_repo.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}