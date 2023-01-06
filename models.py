#Python
from typing import Optional
from enum import Enum

#Pydantic
from pydantic import BaseModel, Field


class HairColor(Enum):
    white = 'white'
    brow = 'brow'
    black = 'black'
    blonde = 'blonde'
    red = 'red'

class Location(BaseModel):
    city: str
    state: str

class Person(BaseModel):
    firstName: str = Field(..., min_lenght=1, max_length=50, example="Carlos" )
    lastName: str =  Field(..., min_lenght=1, max_length=50, example="Lopez")
    age: int = Field(..., gt=0, le=115, example=89)
    hairColor: Optional[HairColor] = Field(default= None, example="brow")
    isMarried: Optional[bool] = Field(default=None, example=False)
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


class PersonOut(BaseModel):
    firstName: str = Field(..., min_lenght=1, max_length=50, example="Carlos" )
    lastName: str =  Field(..., min_lenght=1, max_length=50, example="Lopez")
    age: int = Field(..., gt=0, le=115, example=89)
    hairColor: Optional[HairColor] = Field(default= None, example="brow")
    isMarried: Optional[bool] = Field(default=None, example=False)
