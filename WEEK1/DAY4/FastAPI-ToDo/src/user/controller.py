from src.user.dtos import UserSchema, LoginSchema
from sqlalchemy.orm import Session
from src.user.models import UserModel
from fastapi import HTTPException, status, Request
from pwdlib import PasswordHash
from datetime import datetime, timedelta
import jwt
from jwt.exceptions import InvalidTokenError
from src.utils.settings import settings

password_hash = PasswordHash.recommended()

def get_password_hash(password):
    return password_hash.hash(password)

def verify_password(plain_password, hashed_password):
    return password_hash.verify(plain_password, hashed_password)


def register(body: UserSchema, db:Session):
    is_user = db.query(UserModel).filter(UserModel.username == body.username).first()
    if is_user:
        raise HTTPException(400, detail="user name exist...")

    is_user = db.query(UserModel).filter(UserModel.email == body.email).first()
    if is_user:
        raise HTTPException(400, detail="Email address exist...")

    hash_password= get_password_hash(body.password)
    new_user = UserModel(
        name = body.name,
        username = body.name,
        hash_password = hash_password,
        email = body.email
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

def login_user(body:LoginSchema, db:Session):
    user = db.query(UserModel).filter(UserModel.username == body.username).first()
    if not user:
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail="you entered wrong user name!")
    
    if not verify_password(body.password, user.hash_password):
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail="you entered wrong password!")
    # exp_time = datetime.now() + timedelta(seconds =30)

    exp_time = datetime.now() + timedelta(minutes = settings.EXP_TIME)
    token = jwt.encode({"_id":user.id, "exp":exp_time.timestamp()}, settings.SECRET_KEY, settings.ALGORITHM)


    return {"token": token}

#token send
def is_authenticated(request:Request, db:Session):
    try:    
        token = request.headers.get("Authorization")
        if not token:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="you are unauthorised.")

        token = token.split(" ")[-1]

        data = jwt.decode(token, settings.SECRET_KEY, settings.ALGORITHM)
        user_id = data.get("_id")

        

        
        user = db.query(UserModel).filter(UserModel.id==user_id).first()
        if not user:
            raise HTTPException(status_code =status.HTTP_401_UNAUTHORIZED, detail = "you are unauthorised")


        return user
    
    except InvalidTokenError:
        raise HTTPException(status_code =status.HTTP_401_UNAUTHORIZED, detail = "you are unauthorised")

