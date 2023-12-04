# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from database import Base, engine
from fastapi import FastAPI
from api.test_api.tests import test_router
from api.user_api.users import user_router

app = FastAPI(docs_url='/')

# Create db
Base.metadata.create_all(bind=engine)


# Registration of components
app.include_router(test_router)
app.include_router(user_router)

#Type Get request to get hello world
@app.get('/products', tags=['Products'])
async def All_products():
    return {'message': 'Hello World'}

@app.get('/hello2', tags=['Products'])
async def hello():
    return {'message2': 'Hello World2'}

@app.post('/hello2', tags=['Otabek products'])
async def test_post(name: str, phone: int):
    return {f'Name: {name}, Phone: {phone}'}

@app.put('/change_otabek', tags=['Otabek products'])
async def change_test(name:str, phone:int, email:str):
    return {f'Name: {name}, Phone: {phone}, email: {email}'}

