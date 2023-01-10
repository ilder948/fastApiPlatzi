#Python
from typing import Optional


#FastApi
from fastapi import FastAPI
from fastapi import status
from fastapi import Body, Query, Path, Form


# import Modelos

from models import Person, PersonOut, LoginOut


app = FastAPI()


@app.get(
    path='/', 
    status_code=status.HTTP_200_OK
    )
def home():
    return {'Hello': 8989}

#Request and Response Body

@app.post(
    path='/person/new',
    response_model=PersonOut,
    status_code=status.HTTP_201_CREATED
    )
def createPerson(person: Person = Body(...)):
    return person


# Validaciones Query parameters

@app.get(
    path='/person/detail',
    status_code=status.HTTP_200_OK
    )
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

@app.get(
    path='/person/detail/{person_id}',
    status_code=status.HTTP_201_CREATED
    )
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


@app.post(
    path="/login",
    response_model=LoginOut,
    status_code=status.HTTP_200_OK
)
def login(username: str = Form(...), password: str = Form(...)):
    return LoginOut(username=username)