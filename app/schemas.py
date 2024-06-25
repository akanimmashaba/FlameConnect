from typing import Optional
from datetime import datetime
from pydantic import BaseModel

# User Schemas
class UserCreate(BaseModel):
    email: str
    password: str
    name: str
    age: int
    gender: str
    bio: Optional[str] = None

class UserRead(BaseModel):
    id: int
    email: str
    name: str
    age: int
    gender: str
    bio: Optional[str] = None
    created_at: datetime
    updated_at: datetime

class UserUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    gender: Optional[str] = None
    bio: Optional[str] = None

# Match Schemas
class MatchCreate(BaseModel):
    user_id_1: int
    user_id_2: int

class MatchRead(BaseModel):
    id: int
    user_id_1: int
    user_id_2: int
    matched_at: datetime

# Message Schemas
class MessageCreate(BaseModel):
    match_id: int
    sender_id: int
    receiver_id: int
    content: str

class MessageRead(BaseModel):
    id: int
    match_id: int
    sender_id: int
    receiver_id: int
    content: str
    sent_at: datetime

# Subscription Schemas
class SubscriptionCreate(BaseModel):
    user_id: int
    plan_id: int
    start_date: datetime
    end_date: datetime

class SubscriptionRead(BaseModel):
    id: int
    user_id: int
    plan_id: int
    start_date: datetime
    end_date: datetime

# Photo Schemas
class PhotoCreate(BaseModel):
    user_id: int
    url: str

class PhotoRead(BaseModel):
    id: int
    user_id: int
    url: str

# Plan Schemas
class PlanCreate(BaseModel):
    name: str
    price: float
    duration_days: int

class PlanRead(BaseModel):
    id: int
    name: str
    price: float
    duration_days: int
