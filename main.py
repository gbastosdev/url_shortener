from fastapi  import FastAPI, HTTPException, APIRouter
from fastapi.responses import RedirectResponse
from contextlib import asynccontextmanager
import json
from functions import url_shorten
from models.url import URL
import random

@asynccontextmanager
async def lifespan(app: FastAPI):
    global store
    store = json.loads(url_shorten.shorten_urls())
    print(f"{len(store)} URLs carregadas no store")
    yield
    store.clear()
    print("Cleaning store...")

app = FastAPI(lifespan=lifespan)
router = APIRouter(prefix="/api")

@router.get('/urls')
async def get_urls():
    return store.keys()

@router.get("/urls/{short_code}")
async def redirect(short_code: str):
    url = store.get(short_code)
    if not url:
        raise HTTPException(status_code=404, detail="URL not found")
    return RedirectResponse(url=url)

@router.post("/urls")
async def create_url(body: URL):
    url = body.url
    new_id = random.randint(len(store) + 1, 1000000)
    short_code = url_shorten.to_base62(new_id)
    store[short_code] = url
    return {"short_code": short_code, "url": url}

app.include_router(router)
  