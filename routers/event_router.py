from fastapi import APIRouter,Body,Request,HTTPException,status
from typing import List

from models import Event

router = APIRouter()


@router.get("/",response_description="list all event info",response_model=List[Event])
def list_event(request:Request):
  events = list(request.app.database["scrapy_items_Event"].find(limit=100))
  return events

@router.get("/{id}",response_description="get a single event info by id",response_model=Event)
def find_event(id:str,request:Request):
  if(event := request.app.database["scrapy_items_Event"].find_one({"_id":id}))  is not None :
    return event
  raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail = f"Event with ID {id} not found")
