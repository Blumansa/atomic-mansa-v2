from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        from_attributes = True  # nouvelle version de Pydantic V2

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

