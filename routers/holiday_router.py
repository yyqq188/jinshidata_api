from fastapi import APIRouter,Body,Request,HTTPException,status
from typing import List

from models import Holiday

router = APIRouter()


@router.get("/",response_description="list all holiday info",response_model=List[Holiday])
def list_holiday(request:Request,limit:int):
  holidays = request.app.database["scrapy_items"].find().limit(limit)
  return [e for e in holidays]

@router.get("/{id}",response_description="get a single holiday info by id",response_model=Holiday)
def find_holiday(id:str,request:Request):
  holiday = request.app.database["scrapy_items"].find_one({"_id":id})
  if holiday is not None:
    return holiday
  raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail = f"Event with ID {id} not found")
