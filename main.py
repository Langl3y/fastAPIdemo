from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from sqlalchemy.orm import Session, Mapped

from database import SessionLocal, engine
from models import Teacher, Student, User, Base
from routers import students, teachers

Base.metadata.create_all(bind=engine)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()
app.include_router(students.router, prefix="/students")
app.include_router(teachers.router, prefix="/teachers")


class UserInDB(User):
    hashed_password: Mapped[str]


def fake_hashed_password(password: str):
    return "hashedpassword" + password


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


def get_user(username: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.name == username).first()
    return user


def fake_token_decode(token):
    user = get_user(token)

    return user


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    user = fake_token_decode(token)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user


async def get_current_active_user(current_user: Annotated[User, Depends(get_current_user)]):
    if current_user.is_disabled:
        raise HTTPException(status_code=400, detail="Inactive user")

    return current_user


@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = get_user(form_data.username)

    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    user = UserInDB
    hashed_password = fake_hashed_password(form_data.password)

    if not hashed_password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {"access_token": user.name, "token_type": "bearer"}


@app.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user
