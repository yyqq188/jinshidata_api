from fastapi import FastAPI
from dotenv import load_dotenv
from pymongo import MongoClient
from routers.economics_router import router as economics_router
from routers.event_router import router as event_router
from routers.holiday_router import router as holiday_router
from fastapi import Request
from pathlib import Path
import os
from fastapi.responses import HTMLResponse
#部署到render时,需要注释该行
load_dotenv(Path(Path.home(),"env_config",".env_jinshidata_api"),override=True)

app = FastAPI()

@app.on_event("startup")
def startup_db_client():
  app.mongodb_client = MongoClient(os.getenv("MONGO_URI"))
  app.database = app.mongodb_client[os.getenv("MONGO_DATABASE")]
  print("Connected mongodb")

@app.on_event("shutdown")
def shutdown_db_client():
  app.mongodb_client.close()


@app.get("/",response_class=HTMLResponse)
def home(request:Request):
  return """
<html>
        <body align="center">
            <h1>使用方法</h1>
            <h2>1.经济信息</h2>
            <p>https://jinshidata-api.onrender.com/economics/{year}/{month}/{day}/[?limit=10]</p>
            <h2>2.事件信息</h2>
            <p>https://jinshidata-api.onrender.com/event/{year}/{month}/{day}/[?limit=10]</p>
            <h2>3.假期信息</h2>
            <p>https://jinshidata-api.onrender.com/holiday/{year}/{month}/{day}/[?limit=10]</p>
            <h3>ps : limit是可选的,缺省的话,会将该天的所有信息返回 </h3>
            <h3>例如</h3>
            <p>https://jinshidata-api.onrender.com/economics/2023/09/04/?limit=10</p>
            <p>https://jinshidata-api.onrender.com/economics/2023/09/04</p>
            
            
            <h3>目前爬取了并开放了2015年至今的信息</h3>
            <p>后续会逐步扩充API数据,建议收藏</p>
        </body>
</html>

"""
 

app.include_router(economics_router,tags=["economics"],prefix="/economics")
app.include_router(event_router,tags=["event"],prefix="/event")
app.include_router(holiday_router,tags=["holiday"],prefix="/holiday")