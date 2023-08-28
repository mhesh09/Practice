from fastapi import FastAPI
from pydantic import BaseModel

# Create a data model
class Item(BaseModel):
    name:str
    description: str | None = None
    price: float
    tax: float | None = None

app = FastAPI()

#Request body are passed through above created Model from pydantic
@app.post("/items/")
async def create_item(item: Item):
    item_dict = dict(item)
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax":price_with_tax})#Updating dictionary
    return item_dict

#Example of passing parameter plus  request body
@app.put("/items/{item_id}")
async def create_item(item_id:int, item:Item):
    return {"item_id":item_id,**item.model_dump()}#model_dump convert Data Model to dictionary type

#Example of passing parameter pus request body and query parameter
@app.put("/anotheritems/{item_id}")
async def another_create_item(item_id:int, item:Item,q:str | None = None):
    result = {"item_id":item_id,**item.model_dump()}
    if q:
        result.update({"q":q})
    return result