#Python
from typing import Optional
from enum import Enum

#Pydantic
from pydantic import BaseModel, Field

#FastApi
from fastapi import FastAPI
from fastapi import Body, Query, Path


app = FastAPI()

#Models

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


@app.get('/')
def home():
    return {'Hello': 8989}

#Request and Response Body

@app.post('/person/new')
def createPerson(person: Person = Body(...)):
    return {'DATA': [person], 'COUNT': len([person])}


# Validaciones Query parameters

@app.get('/person/detail')
def show_person(
    name: Optional[str] = Query(
        None, 
        min_length=1, 
        max_length=50,
        title='Person Name',
        description="this is the person name, It's between 1 and 500 characteres",
        example="Rocio"
        ),
    age: str = Query(
        ...,
        title='Person Age',
        description="this is the person age, It's required",
        example=56
        )
    ):
    return {name: age}


#validaciones path parameters

@app.get('/person/detail/{person_id}')
def show_person(
    person_id: int = Path(
        ...,
        gt=0,
        name='Person Id',
        description="this is the person id, It's required",
        example= 123
        )
):
    return {'personId': person_id}


#Validations Request Body

@app.put("/person/{person_id}")
def update_person(
    person_id: int = Path(
        ...,
        title="Person Id",
        description="Id de la persona",
        gt=0
    ),
    person: Person = Body(...),
    #location: Location = Body(...)
):
    #result = person.dict()
    #result.update(location.dict())
    return {person}