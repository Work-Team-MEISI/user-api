from fastapi import FastAPI, HTTPException
from schemas import User

app = FastAPI()

@app.get("/")
async def root():
   return {"Hello world!"}