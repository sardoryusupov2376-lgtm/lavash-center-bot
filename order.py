from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, JSON
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Order(Base):
    """User orders"""
    __tablename__ = 'orders'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)  # Foreign key
    
    # Order info
    items = Column(JSON)  # [{product_id, quantity, price}, ...]
    total_price = Column(Float)
    
    # Discounts
    discount_percent = Column(Float, default=0)  # 0-15%
    discount_amount = Column(Float, default=0)
    final_price = Column(Float)
    
    # Promo code
    promo_code = Column(String(50), nullable=True)
    
    # Delivery
    delivery_address = Column(String(255))
    delivery_lat = Column(Float)
    delivery_lon = Column(Float)
    delivery_phone = Column(String(20))
    
    # Taxi
    taxi_type = Column(Integer, nullable=True)  # 1266=Uber, 1228=Yandex
    taxi_order_id = Column(String(100), nullable=True)
    
    # Status
    status = Column(String(50), default='pending')  # pending, paid, preparing, delivering, completed
    payment_method = Column(String(50), nullable=True)  # click, payme, cash
    
    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow)
    completed_at = Column(DateTime, nullable=True)
    
    def __repr__(self):
        return f"<Order {self.id} - {self.final_price}>"