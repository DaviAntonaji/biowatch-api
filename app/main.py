from fastapi import FastAPI
from app.controllers import auth_controller, profile_controller
from app.database import engine
from app.models import user_model

user_model.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth_controller.router)
app.include_router(profile_controller.router)