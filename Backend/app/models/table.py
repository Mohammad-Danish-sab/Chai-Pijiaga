import enum
from datetime import datetime
from sqlalchemy import String, Integer, Enum, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.database import Base


class TableStatus(str, enum.Enum):
    AVAILABLE = "AVAILABLE"
    RESERVED = "RESERVED"
    OCCUPIED = "OCCUPIED"
    CLEANING = "CLEANING"
    MAINTENANCE = "MAINTENANCE"


class Table(Base):
    __tablename__ = "tables"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    table_number: Mapped[str] = mapped_column(
        String(20), unique=True, nullable=False, index=True
    )
    capacity: Mapped[int] = mapped_column(Integer, nullable=False)
    status: Mapped[TableStatus] = mapped_column(
        Enum(TableStatus), default=TableStatus.AVAILABLE, nullable=False
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    bookings = relationship("Booking", back_populates="table")
    orders = relationship("Order", back_populates="table")