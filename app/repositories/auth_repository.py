from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from app.models.user_model import User
from app.schemas.auth_schema import UserCreate
from passlib.context import CryptContext
from jose import JWTError, jwt
from app.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class AuthRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_user_by_email(self, email: str):
        return self.db.query(User).filter(User.email == email).first()

    def create_user(self, user_create: UserCreate):
        hashed_password = pwd_context.hash(user_create.password)
        db_user = User(
            name=user_create.name,
            email=user_create.email,
            hashed_password=hashed_password
        )
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def verify_password(self, plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)

    def create_access_token(self, data: dict):
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
        return encoded_jwt

    def authenticate_user(self, email: str, password: str):
        user = self.get_user_by_email(email=email)
        if not user or not self.verify_password(password, user.hashed_password):
            return None
        return user