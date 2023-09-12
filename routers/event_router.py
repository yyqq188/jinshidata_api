from fastapi import APIRouter,Body,Request,HTTPException,status
from typing import Optional

from models import Event

router = APIRouter()


@router.get("/{year}/{month}/{day}",response_description="list all event info")
def list_event(request:Request,year:str,month:str,day:str,limit:Optional[int] = 1000):
  events = request.app.database["scrapy_items_Event"].find({"url":f"https://cdn-rili.jin10.com/web_data/{year}/daily/{month}/{day}/event.json"},
                                                           {"_id":0}).limit(limit)
  return [e for e in events]

@router.get("/{id}",response_description="get a single event info by id")
def find_event(id:str,request:Request):
  event = request.app.database["scrapy_items_Event"].find_one({"_id":id})
  if event is not None:
    return event
  raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail = f"Event with ID {id} not found")
