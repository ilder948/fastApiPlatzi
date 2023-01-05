#Python
from typing import Optional

#Pydantic
from pydantic import BaseModel

#FastApi
from fastapi import FastAPI
from fastapi import Body, Query, Path


app = FastAPI()

#Models


class Location(BaseModel):
    city: str
    state: str

class Person(BaseModel):
    firstName: str
    lastName: str
    age: int
    hairColor: Optional[str] = None
    isMarried: Optional[bool] = False


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
        description="this is the person name, It's between 1 and 500 characteres"
        ),
    age: str = Query(
        ...,
        title='Person Age',
        description="this is the person age, It's required"
        )
    ):
    return {name: age}


#validaciones path parameters

@app.get('/person/detail/{person_id}/car/{car_id}')
def show_person(
    person_id: int = Path(
        ...,
        gt=0,
        name='Person Id',
        description="this is the person id, It's required"
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
    location: Location = Body(...)
):
    result = person.dict()
    result.update(location.dict())
    return {"id": person_id, "person": result}