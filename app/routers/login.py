from fastapi import APIRouter, HTTPException, status
from ..schemas import NewUserResponse, User
from ..utils import conn, cursor
from passlib.context import CryptContext
from .. import oauth2


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

router = APIRouter()


@router.post("/login")
def login(user_credentials: User):
    cursor.execute("SELECT * FROM users WHERE email = %s", (user_credentials.email,))
    user = cursor.fetchone()

    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="invalid credentials!")

    if not pwd_context.verify(user_credentials.password, user["password"]):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="invalid credentials")

    access_token = oauth2.create_access_token(data={"user_id": user["id"]})
    return {"access_token": access_token, "token_type": "Bearer"}
