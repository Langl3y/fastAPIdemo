from pydantic import BaseModel


class User(BaseModel):
    name: str
    fullname: str
    email: str
    role: str
    is_disabled: bool = False


class UserInDB(User):
    hashed_password: str
