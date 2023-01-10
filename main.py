#Python
from typing import Optional


from pydantic import EmailStr


#FastApi
from fastapi import FastAPI
from fastapi import status
from fastapi import Body, Query, Path, Form, Header, Cookie


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

#Cookies and headers parameters

@app.post(
    path="/contact", 
    status_code=status.HTTP_200_OK
)
def contact(
    first_name: str = Form(
        ...,
        max_length=20,
        min_length=1
    ),
    last_name: str = Form(
        ...,
        max_length=20,
        min_length=1
    ),
    email: EmailStr = Form(...),
    message: str = Form(
        ...,
        min_length=20
    ),
    user_agent: Optional[str] = Header(default=None),
    ads: Optional[str] = Cookie(default=None)

):
    return user_agent







# anyio==3.6.2
# click==8.1.3
# dnspython==2.2.1
# email-validator==1.3.0
# fastapi==0.88.0
# h11==0.14.0
# idna==3.4
# pydantic==1.10.4
# python-multipart==0.0.5
# six==1.16.0
# sniffio==1.3.0
# starlette==0.22.0
# typing_extensions==4.4.0
# uvicorn==0.20.0