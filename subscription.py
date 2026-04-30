from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Subscription(Base):
    """Premium subscriptions"""
    __tablename__ = 'subscriptions'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, unique=True)  # Foreign key
    
    # Subscription info
    plan = Column(String(50), default='monthly')  # monthly, quarterly, yearly
    price = Column(Float, default=50000)  # 50,000 som
    
    # Status
    is_active = Column(Boolean, default=True)
    started_at = Column(DateTime, default=datetime.utcnow)
    expires_at = Column(DateTime)
    renewed_at = Column(DateTime, nullable=True)
    
    # Payment
    payment_status = Column(String(50))  # pending, completed, failed
    transaction_id = Column(String(100), nullable=True)
    
    def __repr__(self):
        return f"<Subscription User:{self.user_id} - {self.plan}>"