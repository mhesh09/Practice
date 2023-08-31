from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()



class Image(BaseModel):
    url:HttpUrl #It's a pydantic Type. For detail https://docs.pydantic.dev/latest/usage/types/types/
    name:str


class Item(BaseModel):
    name:str
    description: str | None = None
    price: float
    tax: float | None = None
    # tags: list[str] = []
    #Created a list in Model.For typing purpose we have to use list[str]
    anothertags: set[str] = set()
    #When we want a non-repeated or non-redundant value we use set
    image:Image | None = None
    #For nested Purpose

@app.put("/items/{items_id}")
async def read_items(items_id:int, item:Item):
    results = {"item_id":items_id,"item":item}
    return results

@app.post("/products")
async def read_product(*,images:list[Image]):
    return images
#It return list of dictionary of Image Class

@app.post("/index-weights/")
async def create_index_weights(weights: dict[int, float]):
    return weights
#It converts JSON value. It convert key to integer and value to float. 
#In JSON, key will be always in String. Even though being in string if the key contain pure integer it validate it to integer.
#in return we yield integer as key and float as value.



