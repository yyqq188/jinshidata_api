from fastapi import FastAPI
from dotenv import load_dotenv
from pymongo import MongoClient
from routers.economics_router import router as economics_router
from routers.event_router import router as event_router
from routers.holiday_router import router as holiday_router
from fastapi import Request
from pathlib import Path
import os
#部署到render时,需要注释该行
# load_dotenv(Path(Path.home(),"env_config/.env_jinshidata_api"),override=True)

app = FastAPI()

@app.on_event("startup")
def startup_db_client():
  app.mongodb_client = MongoClient(os.getenv("MONGO_URI"))
  app.database = app.mongodb_client[os.getenv("MONGO_DATABASE")]
  print("Connected mongodb")

@app.on_event("shutdown")
def shutdown_db_client():
  app.mongodb_client.close()


@app.get("/")
def aa(request:Request):
  # data = MongoClient(config['MONGO_URI'])["scrapy_test_db"]
  data = request.app.database

  r = data["scrapy_items_Economics"].find().limit(10)
  return [e for e in r]
  


# app.include_router(economics_router,tags=["economics"],prefix="/economics")
# app.include_router(event_router,tags=["event"],prefix="/event")
# app.include_router(holiday_router,tags=["holiday"],prefix="/holiday")