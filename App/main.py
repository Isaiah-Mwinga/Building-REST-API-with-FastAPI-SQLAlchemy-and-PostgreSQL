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

