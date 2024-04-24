from fastapi import FastAPI

app = FastAPI()

from pydantic import BaseModel

class_list = []


class Item(BaseModel):
    name: str

class Element(BaseModel):
    number: int

@app.get('/classes')
async def get_items():
    return class_list

@app.post('/add')
async def add_item(item: Item):
    class_list.append(item.name)
    return {'message': 'done'}

@app.delete('/remove')
async def remove_item(element: Element):
    class_list.pop(element.number)
    return {'message': 'done'}