from fastapi import FastAPI, Depends
from pydantic import BaseModel, EmailStr
from typing import List

app = FastAPI()


class UserSignup(BaseModel):
    username: str = "username"
    email: EmailStr
    password: str = "example1234"


users: List[UserSignup] = []


class Settings(BaseModel):
    app_name: str = "Tea App"
    admin_email: str = "admin@ai.com"


def get_settings():
    return Settings()


@app.get("/user")
def user():
    return users


@app.post("/signup")
def signup(user: UserSignup):
    users.append(user)
    return {"message": f"User {user.username} is signup successfully."}


@app.get("/settings")
def settings(setting: Settings = Depends(get_settings)):
    return setting
