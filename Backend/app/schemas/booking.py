from datetime import datetime, date, time
from pydantic import BaseModel, ConfigDict, Field
from app.models.table import TableStatus
from app.models.booking import BookingStatus


class TableCreate(BaseModel):
    table_number: str
    capacity: int = Field(gt=0)


class TableUpdate(BaseModel):
    table_number: str | None = None
    capacity: int | None = Field(default=None, gt=0)
    status: TableStatus | None = None


class TableResponse(BaseModel):
    id: int
    table_number: str
    capacity: int
    status: TableStatus

    model_config = ConfigDict(from_attributes=True)


class BookingCreate(BaseModel):
    table_id: int
    booking_date: date
    start_time: time
    end_time: time
    guests: int = Field(gt=0)


class BookingStatusUpdate(BaseModel):
    status: BookingStatus


class BookingResponse(BaseModel):
    id: int
    booking_number: str
    user_id: int
    table_id: int
    booking_date: date
    start_time: time
    end_time: time
    guests: int
    status: BookingStatus
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)