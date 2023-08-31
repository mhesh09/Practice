from typing import Annotated
from fastapi import FastAPI, Query, Path, Body
from pydantic import BaseModel


app = FastAPI()

class Item(BaseModel):
    name:str
    description:str | None = None
    price:float
    tax:float | None = None


class User(BaseModel):
    username:str
    full_name: str | None = None

@app.put("/items/{item_id}")
#If there is no data from request body. By default, we can assign NULL
async def read_items(item_id:Annotated[int,Path(title="The ID of the item to get",ge=0,le=1000)],q:str | None = None, item:Item|None =None):
    results = {"item_id":item_id}
    if q:
        results.update({"q":q})
    if item:
        results.update({"item":item})
    return results

@app.post("/products/{product_id}")
#Used a multiple request body.Item and User goes into the nested form in request.
async def read_products(product_id:int,item:Annotated[Item,Body(embed=True)],user:User,importance:Annotated[int, Body(gt=0)]):
    #To introduce a singular value which is importance in this function we have to mention Body() function in order to treat it like body parameter.
    #In body function we can use our query.
    results = {"productId":product_id,"Item":item,"User":user}
    return results