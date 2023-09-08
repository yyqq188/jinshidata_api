from fastapi import APIRouter,Body,Request,HTTPException,status
from typing import List

from models import Holiday

router = APIRouter()


@router.get("/",response_description="list all holiday info",response_model=List[Holiday])
def list_holiday(request:Request):
  holidays = list(request.app.database["scrapy_items"].find(limit=100))
  return holidays

# @router.get("/{id}",response_description="get a single holiday info by id",response_model=Holiday)
# def find_holiday(id:str,request:Request):
#   if(holiday := request.app.database["scrapy_items"].find_one({"_id":id}))  is not None :
#     return holiday
#   raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail = f"Event with ID {id} not found")
