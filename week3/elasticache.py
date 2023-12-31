import os
import time
import json
import redis
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

class Redis:
    def __init__(self):
        self.client = redis.StrictRedis(
            host=os.getenv("REDIS_ENDPOINT"),
            port=os.getenv("REDIS_PORT"),
            db=0,
            decode_responses=True,
        )
    
    def set(self, key, value):
        return self.client.set(key, value)
    
    def get(self, key):
        return self.client.get(key)
    
    def delete(self, key):
        return self.client.delete(key)
    
if __name__ == "__main__":
    redis_client = Redis()
    
    df = pd.read_csv('titanic.csv')
    start = time.time()
    for idx, row in df.iterrows():
        redis_key = row["PassengerId"]
        redis_value = json.dumps(row.to_dict())
        redis_client.set(redis_key, redis_value)
    end = time.time()

    print(f"Upload records to redis: {end - start} seconds")
    print(f"Upload records to redis: {(end - start) / len(df)} seconds per record")
    print(redis_client.get(1))
    print(redis_client.get(891))