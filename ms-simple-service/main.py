from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Public endpoint"}

@app.get("/secure-data")
async def read_secure_data(token: str = Depends(oauth2_scheme)):
    return {"message": "This is a secure endpoint!"}