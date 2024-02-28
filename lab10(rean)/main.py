from typing import Optional
from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel


app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/hello")
def hello(name:str):
    return {"Hello": name}

@app.get("/test")
def test(request:str, reply:str):
    return {"Request": request, "Reply": reply}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

if __name__== "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info")

todos = [
    {
        "id" : "1",
        "Activity" : "Jpgging for 2 hours at 7:00 AM."
    },
    {
        "id" : "2",
        "Activity" : "Writing 3 pages of my new book at 2:00 PM."
    }
]

@app.get("/", tags=['root'])
async def root() -> dict:
    return {"Ping" : "Pong"}

@app.get("/todo", tags=['Todos'])
async def get_todos() -> dict:
    return {"Data": todos}

class Todo(BaseModel):
    id: str
    Activity: str

# Post - - > Create Todo
@app.post("/todo", tags=["Todos"])
async def add_todo(todo:Todo):
    return todo
    print(todo)
    todos.append(todo)
    return {
        "data": "A Todo is Added!"
    }

@app.put("/todo/{id}", tags=["Todos"])
async def update_todo(id: int, body:dict) -> dict:
    for todo in todos:
        if (int(todo["id"])) == id:
            todo["Activity"] = body["Activity"]
            return{
                "data" : f"Todo with id {id} has been updated"
            }
    return{
        "data" : f"This Todo with id {id} is not found!"
    }

@app.delete("/Todo/{id}", tags=["Todos"])
async def delete_todo(id : int) -> dict:
    for todo in todos:
        if int(todo["id"]) == id:
            todos.remove(todo)
            return {
                "data" : f"Todo with id {id} has been deleted!"
            }
    return {
        "data" : f"Todo with id {id} was not found!"
    }

