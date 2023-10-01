from fastapi import APIRouter, HTTPException, status
from ..schemas import NewUserResponse, User
from ..utils import conn, cursor
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

router = APIRouter()


@router.post("/users", status_code=status.HTTP_201_CREATED, response_model=NewUserResponse)
def create_user(user: User):
    cursor.execute(
        "INSERT INTO users (email,password) VALUES(%s,%s) RETURNING *", (user.email, pwd_context.hash(user.password))
    )
    print(cursor)
    new_user = cursor.fetchone()
    print(new_user)
    conn.commit()
    return new_user
