from typing import List, Optional, List
from uuid import UUID, uuid4
from pydantic import BaseModel
from enum import Enum
#in this file i am making the base
#of the user infos

class Gender(str, Enum):
    male = 'male'
    female = 'female'

class Role(str, Enum):
    admin = 'admin'
    user = 'user'
    student = 'student'

class User(BaseModel):
    id: Optional[UUID] = uuid4()
    first_name: str
    last_name:str
    middle_name: Optional[str]
    gender: Gender
    roles: List[Role]

class UserUptadeRequest(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    middle_name: Optional[str] = None
    roles: Optional[List[Role]] = None
