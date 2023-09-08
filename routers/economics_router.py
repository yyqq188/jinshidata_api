from fastapi import APIRouter,Body,Request,HTTPException,status
from typing import List

from models import Economics

router = APIRouter()


@router.get("/",response_description="list all economics info",response_model=List[Economics])
def list_info(request:Request):
  # economics = list(request.app.database["scrapy_items_Economics"].find({}))
  # return economics
  print(request.app.database)

@router.get("/{id}",response_description="get a single economics info by id",response_model=Economics)
def find_info(id:str,request:Request):
  if(economic := request.app.database["scrapy_items_Economics"].find_one({"_id":id}))  is not None :
    return economic
  raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail = f"Info with ID {id} not found")
