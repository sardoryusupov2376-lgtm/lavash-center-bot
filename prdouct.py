from sqlalchemy import Column, Integer, String, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Category(Base):
    """Product categories"""
    __tablename__ = 'categories'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True)  # Lavash, Burger, Donar, Ichimliklar, Fri
    emoji = Column(String(10))
    
    def __repr__(self):
        return f"<Category {self.name}>"

class Product(Base):
    """Products/Menu items"""
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True)
    category_id = Column(Integer)  # Foreign key
    name = Column(String(100))
    description = Column(String(500))
    price = Column(Float)  # Narxi
    image_url = Column(String(500), nullable=True)
    is_available = Column(Boolean, default=True)
    
    def __repr__(self):
        return f"<Product {self.name} - {self.price}>"