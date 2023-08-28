from fastapi import FastAPI
from enum import Enum
app = FastAPI()

@app.get("/")
async def aroot():
    return {"message":"Hello World!"}

@app.get("/items/{item_id}")
async def displayItem(item_id:int):
    return {"item_id":item_id}

class ModelName(str,Enum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"

@app.get("/models/{model_name}")
async def checkModelIsExist(model_name:ModelName):
    if model_name is ModelName.RED:
        return {"message":model_name}
    
    if model_name == "green":
        return {"model":"GREEN"}
    
    return {"model":model_name}
