from typing import Optional, List
from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(index=True, unique=True)
    hashed_password: str
    name: str
    age: int
    gender: str
    bio: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    matches: List["Match"] = Relationship(back_populates="users")
    sent_messages: List["Message"] = Relationship(back_populates="sender")
    received_messages: List["Message"] = Relationship(back_populates="receiver")
    subscriptions: List["Subscription"] = Relationship(back_populates="user")
    photos: List["Photo"] = Relationship(back_populates="user")

class Match(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id_1: int = Field(foreign_key="user.id")
    user_id_2: int = Field(foreign_key="user.id")
    matched_at: datetime = Field(default_factory=datetime.utcnow)

    users: List["User"] = Relationship(back_populates="matches")

class Message(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    match_id: int = Field(foreign_key="match.id")
    sender_id: int = Field(foreign_key="user.id")
    receiver_id: int = Field(foreign_key="user.id")
    content: str
    sent_at: datetime = Field(default_factory=datetime.utcnow)

    sender: "User" = Relationship(back_populates="sent_messages")
    receiver: "User" = Relationship(back_populates="received_messages")

class Subscription(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    plan_id: int = Field(foreign_key="plan.id")
    start_date: datetime
    end_date: datetime

    user: "User" = Relationship(back_populates="subscriptions")
    plan: "Plan" = Relationship(back_populates="subscriptions")

class Photo(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    url: str

    user: "User" = Relationship(back_populates="photos")

class Plan(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    price: float
    duration_days: int

    subscriptions: List["Subscription"] = Relationship(back_populates="plan")
