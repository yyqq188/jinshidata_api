from fastapi import APIRouter,Body,Request,HTTPException,status
from typing import Optional
router = APIRouter()

# 把这块先注释掉,response_model=List[Economics] ,后期在想办法修改
# @router.get("/",response_description="list all economics info",response_model=List[Economics])
@router.get("/{year}/{month}/{day}",response_description="list all economics info")
def list_info(request:Request,year:str,month:str,day:str,limit:Optional[int] = 1000):
  # r = request.app.database["scrapy_items_Economics"].find({},{"_id":0,"affect":1}).limit(10)
  # return [e for e in r]

  r = request.app.database["scrapy_items_Economics"].find({"url":f"https://cdn-rili.jin10.com/web_data/{year}/daily/{month}/{day}/economics.json"},{"_id":0}).limit(limit)
  return [e for e in r]
  

@router.get("/{id}",response_description="get a single economics info by id")
def find_info(id:str,request:Request):
  economic = request.app.database["scrapy_items_Economics"].find_one({"_id":id})
  if economic is not None :
    return economic
  raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail = f"Info with ID {id} not found")
