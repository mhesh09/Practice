from typing import Annotated
from fastapi import FastAPI, Query, Path, Body
from pydantic import BaseModel, Field

app = FastAPI()

class Item(BaseModel):
    name:str
    description: str | None = Field(default=None,title="This is descrtiption",max_length=100)
    #We can use query in Field same like Path & Query 
    price:float = Field(title="This is about price",gt=0)
    tax:float | None = None

@app.post('/items/{items_id}')
async def read_items(items_id:Annotated[int , Path(gt=0)],item:Annotated[Item, Body(embed=True) ]):
    results ={"itemId":items_id,"item":item}
    return results