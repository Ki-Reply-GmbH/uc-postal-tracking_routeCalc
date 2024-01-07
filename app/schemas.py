from pydantic import BaseModel
from datetime import datetime
from typing import Optional


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
