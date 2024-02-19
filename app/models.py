from sqlalchemy import Integer, Column, ForeignKey, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)

class Package(Base):
    __tablename__ = "packages"

    id = Column(String, primary_key=True, index=True)
    status = Column(String)
    description = Column(String)
    last_updated = Column(DateTime, default=datetime.utcnow)

class Route(Base):
    __tablename__ = "routes"

    id = Column(Integer, primary_key=True, index=True)
    package_id = Column(String, ForeignKey("packages.id"))
    current_location = Column(String)
    destination = Column(String)
    estimated_arrival = Column(DateTime)