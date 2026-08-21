from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field


class CategoryCreate(BaseModel):
    name: str
    description: str | None = None


class CategoryUpdate(BaseModel):
    name: str | None = None
    description: str | None = None


class CategoryResponse(BaseModel):
    id: int
    name: str
    description: str | None = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class MenuItemCreate(BaseModel):
    category_id: int
    name: str
    description: str | None = None
    price: float = Field(gt=0, description="Price must be positive")
    image_url: str | None = None
    stock: int = Field(ge=0, default=0)
    is_available: bool = True


class MenuItemUpdate(BaseModel):
    category_id: int | None = None
    name: str | None = None
    description: str | None = None
    price: float | None = Field(default=None, gt=0)
    image_url: str | None = None
    stock: int | None = Field(default=None, ge=0)
    is_available: bool | None = None


class MenuItemStockUpdate(BaseModel):
    stock: int = Field(ge=0)


class MenuItemAvailabilityUpdate(BaseModel):
    is_available: bool


class MenuItemResponse(BaseModel):
    id: int
    category_id: int
    name: str
    description: str | None = None
    price: float
    image_url: str | None = None
    stock: int
    is_available: bool
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)