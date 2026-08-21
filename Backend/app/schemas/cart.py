from pydantic import BaseModel, ConfigDict, Field
from app.schemas.menu_item import MenuItemResponse


class CartItemCreate(BaseModel):
    menu_item_id: int
    quantity: int = Field(gt=0, default=1)


class CartItemUpdate(BaseModel):
    quantity: int = Field(gt=0)


class CartItemResponse(BaseModel):
    id: int
    menu_item_id: int
    quantity: int
    menu_item: MenuItemResponse
    item_total: float

    model_config = ConfigDict(from_attributes=True)


class CartResponse(BaseModel):
    id: int
    items: list[CartItemResponse]
    grand_total: float

    model_config = ConfigDict(from_attributes=True)