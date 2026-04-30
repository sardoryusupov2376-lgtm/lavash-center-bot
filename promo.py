from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class PromoCode(Base):
    """Promo codes"""
    __tablename__ = 'promo_codes'
    
    id = Column(Integer, primary_key=True)
    code = Column(String(50), unique=True)  # WELCOME10, LAVASH50
    discount_percent = Column(Float)  # 10, 50 va h.k.
    description = Column(String(255))
    
    # Limits
    max_uses = Column(Integer, nullable=True)  # Cheksiz bo'lsa NULL
    used_count = Column(Integer, default=0)
    
    # Timing
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    expires_at = Column(DateTime, nullable=True)
    
    def __repr__(self):
        return f"<PromoCode {self.code} - {self.discount_percent}%>"