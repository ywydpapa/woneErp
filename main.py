import templates
from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse(request=request, name="/index.html", context={"request": request, "page_title": "업무 대시보드"})


