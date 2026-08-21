from datetime import datetime
from pydantic import BaseModel, ConfigDict
from app.models.order import OrderType, OrderStatus
from app.schemas.menu_item import MenuItemResponse


class OrderCreate(BaseModel):
    order_type: OrderType
    table_id: int | None = None  # Mandatory for DINE_IN, None for TAKEAWAY


class OrderStatusUpdate(BaseModel):
    status: OrderStatus


class OrderItemResponse(BaseModel):
    id: int
    menu_item_id: int
    quantity: int
    price: float
    subtotal: float
    menu_item: MenuItemResponse

    model_config = ConfigDict(from_attributes=True)


class OrderResponse(BaseModel):
    id: int
    order_number: str
    user_id: int
    table_id: int | None
    order_type: OrderType
    total_amount: float
    order_status: OrderStatus
    created_at: datetime
    items: list[OrderItemResponse]

    model_config = ConfigDict(from_attributes=True)