from fastapi import FastAPI, HTTPException
from schemas import User

app = FastAPI()

users = []

@app.post("/users/create")
async def create(user: User):
    check_user = [u for u in users if u.username == user.username]

    if check_user:
        raise HTTPException(status_code=400, detail="Username already exists!")

    if users:
        user.id = users[-1].id + 1
    else:
        user.id = 1 
    
    users.append(user)

    return {**{"id": user.id},**{"message": "Created with success!"}}

@app.get("/users/{id}")
async def detail(id):
    user = [u for u in users if str(u.id) == id]

    if user:
        return user[0]
    else:
        raise HTTPException(status_code=404, detail=f"User with id {id} doesn't exist!")
