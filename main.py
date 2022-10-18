#Here i import the fastApi, you must
#install uvicorn[standard] and fastapi with pip
#All credits to "Amigoscode" who make this code
#https://www.youtube.com/c/amigoscode
#to start the server we use the code uvicorn main:app --reload
#if we add /docs in the url we go to a very cool page :) or there is a very cool extension for api is thunder client
#both do the same thing but /docs bring more information
from uuid import UUID
from fastapi import FastAPI, HTTPException
from typing import List
from models import Gender, User, Role

#here we call the fastApi function
app = FastAPI() 
#here we pass the root of fastapi

db: List[User] = [
    User(id=UUID('817d6f0d-b3e0-4af7-bf3c-4f3e89c2f1b8'), 
    first_name="Belle", 
    last_name="Bellinha", 
    gender=Gender.female,
    roles=[Role.student]),
    User(id=UUID('7508a784-1f16-49ef-9145-77cd79f747fa'),
    first_name="Wilson",
    last_name="delas", 
    middle_name="rei",
    gender=Gender.male,
    roles=[Role.admin, Role.user])
]

@app.get("/")
async def root():
    return {"Hello": "Mundo"}

@app.get("/api/v1/users")
async def fetch_users():
    return db;

@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"id" : user.id}

@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404,
        detail=f'user with id: {user_id} does not exist'
    )