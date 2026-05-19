from sqlalchemy import Boolean, Column, Date, DateTime, ForeignKey, Float, Integer, JSON, String, Enum as SQLEnum
from app.database.database import Base
from datetime import datetime, timezone
from app.core.enum import UserRole


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)

    full_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    user_name = Column(String, unique=True, nullable=False)
    hashed_password = Column(String)

    is_email_verified = Column(Boolean, nullable=False, default=False)
    role = Column(
        SQLEnum(UserRole),
        default=UserRole.User
    )

    created_at = Column(
        DateTime(timezone=True),
        default= lambda: datetime.now(timezone.utc),
        nullable=False
    )

    updated_at = Column(
        DateTime(timezone=True),
        default= lambda: datetime.now(timezone.utc),
        onupdate= lambda: datetime.now(timezone.utc),
        nullable=False
    )