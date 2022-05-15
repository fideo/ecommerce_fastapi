from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

def generate_html():
    html = open("index.html").read()
    return HTMLResponse(html,status_code=200)

@app.get("/",response_class=HTMLResponse)
async def root():
    return generate_html()
