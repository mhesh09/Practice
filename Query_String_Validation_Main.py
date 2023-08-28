from typing import Annotated
from fastapi import FastAPI, Query


app = FastAPI()

#In query parameter checking its character limit
@app.get("/items/")
#Work of Annotated is used to add meta data
def read_items(q:Annotated[str | None, Query(max_length=50,min_length=10,regex="^fixedquery$") ] = None ):
    result = {"items":[{"item_id":"Foo"},{"item_id":"Bar"}]}
    if q:
        result.update({"q":q})
    return result

#Multiple value/Query parameter list
@app.get("/products/")
def read_products(q:Annotated[list[str]|None,Query()]=["foo","boo"]):
    query_products = {"q":q}
    return query_products

#Playing other Query parameter
@app.get("/books/")
def read_books(q:Annotated[str | None,Query(title="Bright")]=None):
    query_books = {"q":q}
    return query_books