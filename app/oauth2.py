from telnetlib import STATUS
from tkinter.messagebox import RETRY
from jose import JWSError, jwt
from datetime import datetime, timedelta
from rsa import verify
from . import schema, database, models
from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from .config import settings


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
ACCESS_TOKE_EXPIRE_MIMUTE = settings.access_token_expire_minutes 

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes = ACCESS_TOKE_EXPIRE_MIMUTE)
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt

def verify_access_token(token: str, credential_exception):

    try: 
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)

        id: str = payload.get("user_id")
        if id is None:
            raise credential_exception

        token_data = schema.TokenData(id=id)

    except JWSError:
        raise credential_exception

    return token_data

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(database.get_db)):
    credential_exception = HTTPException(status_code= status.HTTP_401_UNAUTHORIZED,
    detail =f"Could not validate credential", headers={"WWW-Authenticate": "Bearer"})

    token = verify_access_token(token, credential_exception) 
    user = db.query(models.User).filter(models.User.id == token.id).first()

    return user
