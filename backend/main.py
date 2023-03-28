'''
Minimal example using fastAPI.
'''
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import HTMLResponse

class Employee(BaseModel):
    first_name: str
    last_name: str
    company: str
    age: int
    phone: Optional[str] = None


app = FastAPI()


@app.get("/")
def hello():
    html_content =  """
        <!doctype html>
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Ay sikan</h1>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

@app.post("/create_employee/")
def create_employee(employee: Employee):
    return {
        "status": "created",
        "data": employee
    }