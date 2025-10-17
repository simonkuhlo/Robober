from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

templates = Jinja2Templates(directory="static")

router = APIRouter()

@router.get("/", response_class=HTMLResponse)
async def get_select(request: Request):
    return templates.TemplateResponse("base.j2", {"request": request})
