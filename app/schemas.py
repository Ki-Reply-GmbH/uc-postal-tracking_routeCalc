from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenRequestForm(BaseModel):
    username: str
    password: str

class User(BaseModel):
    username: str

    class Config:
        orm_mode = True


class PackageBase(BaseModel):
    id: str
    description: Optional[str] = None

class PackageCreate(PackageBase):
    pass

class Package(PackageBase):
    status: str
    last_updated: datetime

    class Config:
        orm_mode = True