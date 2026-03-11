# URL Shortener API

A simple URL shortener REST API built with **FastAPI** and **Redis**.

---

## Requirements

- Python 3.10+
- Redis (local or cloud)

---

## Redis Setup

You need a running Redis instance. Choose one of the options below:

### Option 1 — Docker (recommended)

```bash
docker run -d --name redis -p 6379:6379 redis:alpine
```

### Option 2 — Redis Cloud

Create a free account at [redis.io/cloud](https://redis.io/cloud) and set your connection credentials in the environment variables (see `.env` configuration).

### Option 3 — Local install

Follow the [official Redis installation guide](https://redis.io/docs/getting-started/installation/).

---

## Running the API

### Locally

```bash
pip install -r requirements.txt
python main.py
```

The API will be available at `http://127.0.0.1:8001`.

### With Docker Compose

```bash
docker-compose up -d
```

The API will be available at `http://localhost:8000`.

---

## API Routes

### `POST /api/urls`

Creates a short code for a given URL.

**Request body:**
```json
{
  "longURL": "https://example.com/some/very/long/url"
}
```

**Response:**
```json
{
  "short_code": "aB3xZ",
  "url": "https://example.com/some/very/long/url"
}
```

---

### `GET /api/urls/{short_code}`

Redirects to the original URL associated with the given short code.

**Example:**
```
GET /api/urls/aB3xZ
→ 307 Redirect to https://example.com/some/very/long/url
```

Returns `404` if the short code does not exist.

---

### `GET /api/urls`

Returns all stored URLs in Redis.

**Response:** list of all keys currently stored in the cache.

---

## Interactive Docs

FastAPI provides auto-generated documentation at:

- Swagger UI: `http://127.0.0.1:8001/docs`
- ReDoc: `http://127.0.0.1:8001/redoc`
