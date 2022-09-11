from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Item(BaseModel):
    id:int
    name:str
    description:str
    price:float
    on_offer:bool

    class Config:
        orm_mode=True

@app.get('/items')
def get_all_items():
    pass

@app.get('/item/{item_id}')
def get_an_item(item_id:int):
    pass

@app.post('items')
def create_an_item():
    pass

@app.put('/items')
def update_an_item(item_id:int):
    pass

@app.delete('/items')
def delete_an_item(item_id:int):
    pass
