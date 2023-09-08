import uuid
from pydantic import BaseModel,Field

  # id: str = Field(default_factory=uuid.uuid4,alias="_id")

class Economics(BaseModel):
    id: str = Field(default_factory=uuid.uuid4,alias="_id")
    actual : str = Field(...)
    affect : str = Field(...)
    consensus : str = Field(...)
    country  : str = Field(...)
    id : str = Field(...)
    indicator_id : str = Field(...)
    name : str = Field(...)
    previous : str = Field(...)
    pub_time : str = Field(...)
    pub_time_unix : str = Field(...)
    revised  : str = Field(...)
    show_affect : str = Field(...)
    star : str = Field(...)
    time_period  : str = Field(...)
    time_status : str = Field(...)
    unit : str = Field(...)
    video_url : str = Field(...)
    vip_resource : str = Field(...)
    url : str = Field(...)


class Event(BaseModel):
    id: str = Field(default_factory=uuid.uuid4,alias="_id")
    country : str = Field(...)
    determine : str = Field(...)
    emergencies : str = Field(...)
    event_content : str = Field(...)
    event_time : str = Field(...)
    id : str = Field(...)
    note : str = Field(...)
    people : str = Field(...)
    region : str = Field(...)
    star : str = Field(...)
    vip_resource : str = Field(...)
    url : str = Field(...)


class Holiday(BaseModel):
    id: str = Field(default_factory=uuid.uuid4,alias="_id")
    country : str = Field(...)
    date : str = Field(...)
    exchange_name : str = Field(...)
    id  : str = Field(...)
    name : str = Field(...)
    rest_note : str = Field(...)
    url : str = Field(...)



