#Python
from typing import Optional


#FastApi
from fastapi import FastAPI
from fastapi import Body, Query, Path


# import Modelos

from models import Person,  PersonOut


app = FastAPI()


@app.get('/')
def home():
    return {'Hello': 8989}

#Request and Response Body

@app.post('/person/new', response_model=PersonOut)
def createPerson(person: Person = Body(...)):
    return person


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