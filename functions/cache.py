import redis
import dotenv
import os

dotenv.load_dotenv()

def initialize_cache():
    r = redis.Redis(
        host=os.getenv('REDIS_HOST'),
        port=int(os.getenv('REDIS_PORT')),
        decode_responses=True,
        username="admin",
        password=os.getenv('REDIS_PASSWORD')
    )
    if r.ping():
        print("Connected to Redis successfully!")
        return r
    else:
        print("Failed to connect to Redis.")

def set_cache(key: str, value: str):
    r = redis.Redis(
        host=os.getenv('REDIS_HOST'),
        port=int(os.getenv('REDIS_PORT')),
        decode_responses=True,
        username="admin",
        password=os.getenv('REDIS_PASSWORD'),
    )
    r.set(key, value)