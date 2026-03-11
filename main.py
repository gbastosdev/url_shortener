import uvicorn
import random
from fastapi  import FastAPI, HTTPException, APIRouter
from fastapi.responses import RedirectResponse
from contextlib import asynccontextmanager
from functions import url_shorten
from functions import cache
from models.url import URL

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.conn = cache.initialize_cache()
    print(f"Redis loaded into memory!")
    yield
    app.state.conn.quit()
    print("Closing Redis...")

app = FastAPI(lifespan=lifespan)
router = APIRouter(prefix="/api")

@router.get('/urls')
async def get_urls():
    return app.state.conn

@router.get("/urls/{short_code}")
async def redirect(short_code: str):
    url = app.state.conn.get(short_code)
    if not url:
        raise HTTPException(status_code=404, detail="URL not found")
    return RedirectResponse(url=url)

@router.post("/urls")
async def create_url(body: URL):
    longURL = body.longURL
    new_id = random.randint(len(app.state.conn.keys()) + 1, 1000000)
    short_code = url_shorten.to_base62(new_id)
    app.state.conn.set(short_code, longURL)
    return {"short_code": short_code, "url": longURL}

app.include_router(router)
  
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8001, reload=True)