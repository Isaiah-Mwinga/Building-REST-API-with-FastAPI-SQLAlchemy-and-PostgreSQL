from fastapi import FastAPI,status,HTTPException
from pydantic import BaseModel
from typing import Optional,List
from database import SessionLocal
import models

app = FastAPI()

class Item(BaseModel):
    id:int
    name:str
    description:str
    price:float
    on_offer:bool

    class Config:
        orm_mode=True

db=SessionLocal()        

@app.get('/items{item_id}',response_model=Item,status_code=status.HTTP_200_OK)
def get_an_item(item_id:int): 
    items=db.query(models.Item).filter(models.Item.id==item_id).first()

    return items

@app.get('/item/{item_id}')
def get_an_item(item_id:int):
    pass

@app.post('items',response_model=Item,
          status_code=status.HTTP_201_CREATED)
def create_an_item(item:Item):
    new_item = models.Item(
        name=item.name,
        price=item.price,
        description=item.description,
        on_offer=item.on_offer
    )

    db_item=db.query(models.Item).filter(item.name==new_item.name).first()

    if db_item is not None:
        raise HTTPException(status_code=400, details="Item already exists")
    
    db.add(new_item)
    db.commit()

@app.put('/items/{item_id}')
def update_an_item(item_id:int):
    pass

@app.delete('/items/{item_id}')
def delete_an_item(item_id:int):
    pass
