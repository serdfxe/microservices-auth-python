from urllib.request import Request
from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Public endpoint"}

@app.get("/secure-data")
async def get_my_id(request: Request):
    user_id = request.headers.get("x-user-id")
    
    if not user_id:
        return {"error": "User ID not found"}
    
    return {"id": user_id}