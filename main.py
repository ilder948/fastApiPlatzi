#Python
from typing import Optional

#Pydantic
from pydantic import BaseModel

#FastApi
from fastapi import FastAPI, Body
from fastapi import Body


app = FastAPI()

#Models

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