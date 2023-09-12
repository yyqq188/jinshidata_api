from fastapi import APIRouter,Body,Request,HTTPException,status
from typing import Optional

from models import Holiday

router = APIRouter()


@router.get("/{year}/{month}/{day}",response_description="list all holiday info")
def list_holiday(request:Request,year:str,month:str,day:str,limit:Optional[int] = 1000):
  holidays = request.app.database["scrapy_items"].find({"url":f"https://cdn-rili.jin10.com/data/{year}/{month}{day}/holiday.json"},{"_id":0}).limit(limit)
  return [e for e in holidays]

@router.get("/{id}",response_description="get a single holiday info by id")
def find_holiday(id:str,request:Request):
  holiday = request.app.database["scrapy_items"].find_one({"_id":id})
  if holiday is not None:
    return holiday
  raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail = f"Event with ID {id} not found")
