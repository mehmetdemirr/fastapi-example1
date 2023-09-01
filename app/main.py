from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from fastapi_utils.tasks import repeat_every
import time
from jobs.my_jobs import sheduler

app = FastAPI()

sheduler.start()



@app.on_event("startup")
@repeat_every(seconds=3,wait_first=True)
def period():
    print("mehmet")

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")
list=["mehmet","yusuf","mustafa"]

@app.get("/")
def root(request:Request):
    return templates.TemplateResponse("index.html",{"request":request})

@app.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: int):
    return templates.TemplateResponse("item.html", {"request": request, "id": id,"list":list})

app = FastAPI()



@app.get("/selenium")
async def get_data_with_selenium():
    firefox_options = Options()
    firefox_options.headless = True  # Tarayıcı penceresini gizli modda çalıştır
    
    driver = webdriver.Firefox(options=firefox_options)
    
    url = "https://example.com"  # Verileri çekeceğiniz sitenin URL'si
    driver.get(url)
    page_source = driver.page_source
    
    driver.quit()  # Tarayıcıyı kapat
    
    return page_source

