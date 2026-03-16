import redis
import dotenv
import os

dotenv.load_dotenv()

def initialize_cache():
    r = redis.Redis(
        host=os.getenv('REDIS_HOST'),
        port=int(os.getenv('REDIS_PORT')),
        decode_responses=True,
    )
    if r.ping():
        print("Connected to Redis successfully!")
        return r
    else:
        print("Failed to connect to Redis.")