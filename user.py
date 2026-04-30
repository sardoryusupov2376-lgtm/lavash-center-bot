from sqlalchemy import Column, Integer, String, Boolean, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class User(Base):
    """User model - Free/Premium/Admin"""
    __tablename__ = 'users'
    
    user_id = Column(Integer, primary_key=True)
    telegram_id = Column(Integer, unique=True)
    full_name = Column(String(100))
    phone_number = Column(String(20))
    
    # User type
    is_premium = Column(Boolean, default=False)
    is_admin = Column(Boolean, default=False)
    
    # Premium info
    premium_until = Column(DateTime, nullable=True)
    
    # Lokatsiya
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    address = Column(String(255), nullable=True)
    
    # Chegirma
    free_discount_used = Column(Boolean, default=False)
    total_orders = Column(Integer, default=0)
    
    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f"<User {self.telegram_id} - {self.full_name}>"