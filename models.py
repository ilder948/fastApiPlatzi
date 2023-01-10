#Python
from typing import Optional
from enum import Enum

#Pydantic
from pydantic import BaseModel, Field, EmailStr


class HairColor(Enum):
    white = 'white'
    brow = 'brow'
    black = 'blackfds'
    blonde = 'blonde'
    red = 'red'

class Location(BaseModel):
    city: str
    state: str


class PersonBase(BaseModel):
    firstName: str = Field(..., min_lenght=1, max_length=50, example="Carlos" )
    lastName: str =  Field(..., min_lenght=1, max_length=50, example="Lopez")
    age: int = Field(..., gt=0, le=115, example=89)
    hairColor: Optional[HairColor] = Field(default= None, example="brow")
    isMarried: Optional[bool] = Field(default=None, example=False)

class Person(PersonBase):
    password: str = Field(..., min_length=8)

    # class Config:
    #     schema_extra = {
    #         "example": {
    #             "firstName": "Ildebrando",
    #             "lastName": "Mora Valdes",
    #             "age": 34,
    #             "hairColor": "black",
    #             "isMarried": True,
    #         }            
    #     }


class PersonOut(PersonBase):
    pass


class LoginOut(BaseModel):
    username: str = Field(..., max_length=20, example="Ildebrando")
    message: str = Field(default="login")

