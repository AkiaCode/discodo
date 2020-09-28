import os.path
from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

__directory__ = os.path.dirname(os.path.realpath(__file__))

app = APIRouter()

templates = Jinja2Templates(directory=os.path.join(__directory__, "./templates"))


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("board.html", {"request": request})
