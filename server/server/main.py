import gzip
import json

import uvicorn
from fastapi import Body, FastAPI
from pymongo import MongoClient

MONGO_CONN_STRING = 'mongodb://root:example@db:27017/'

app = FastAPI()

@app.post("/log")
def register_logs(body=Body(...)):
    data = gzip.decompress(body).decode('utf-8')
    with MongoClient(MONGO_CONN_STRING) as client:
        log_db = client.log_db
        log_collection = log_db.log_collection
        for line in data.splitlines():
            r = json.loads(line.strip())
            log_collection.insert_one(r)
    return {"status": "OK"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, log_level="info")
