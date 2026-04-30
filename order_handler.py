"""Zakaya handler - Savat, checkout, chegirma"""

from config import (
    PREMIUM_PRICE,
    PREMIUM_DISCOUNT,
    PREMIUM_LARGE_DISCOUNT,
    FREE_LIMIT_ORDERS,
    FREE_DISCOUNT
)

class ShoppingCart:
    """Savat"""
    def __init__(self, user_id):
        self.user_id = user_id
        self.items = []  # [{product_id, quantity, price}, ...]
    
    def add_item(self, product_id, quantity, price):
        """Taom qo'shish"""
        # TODO: Implement
        self.items.append({
            'product_id': product_id,
            'quantity': quantity,
            'price': price
        })
    
    def remove_item(self, product_id):
        """Taom o'chirish"""
        # TODO: Implement
        pass
    
    def get_total(self):
        """Jami summa"""
        return sum(item['price'] * item['quantity'] for item in self.items)
    
    def clear(self):
        """Savatni o'chirish"""
        self.items = []

def calculate_discount(user_type, total_price, promo_code=None):
    """
    Chegirma hisoblash
    
    Free user:
      - 1-3 zakaya: 1 marta 10% chegirma
      - 4+ zakaya: chegirma yo'q
    
    Premium user:
      - Har vir zakaya: 10%
      - 300,000+ so'm: 15% chegirma
    
    Promo code: +5% qo'shimcha
    """
    discount_percent = 0
    
    if user_type == 'premium':
        discount_percent = PREMIUM_DISCOUNT * 100  # 10%
        if total_price >= 300000:
            discount_percent = PREMIUM_LARGE_DISCOUNT * 100  # 15%
    
    elif user_type == 'free':
        # TODO: User orders sonini tekshirish
        # if user.total_orders < FREE_LIMIT_ORDERS and not user.free_discount_used:
        discount_percent = FREE_DISCOUNT * 100  # 10%
    
    # Promo code qo'shish
    if promo_code:
        # TODO: Promokod database dan olish
        pass
    
    discount_amount = total_price * (discount_percent / 100)
    final_price = total_price - discount_amount
    
    return {
        'discount_percent': discount_percent,
        'discount_amount': discount_amount,
        'final_price': final_price
    }

async def checkout(message, user_id):
    """
    /checkout yoki "Zakaya qilish" button
    
    TODO:
    1. Savat ko'rish
    2. Chegirma hisoblash
    3. Lokatsiya so'rash
    4. Telefon raqam so'rash
    5. Promo kod so'rash (ixtiyoriy)
    6. To'lov usuli tanlash
    """
    # TODO: Implement full checkout flow
    pass

async def apply_promo_code(message, user_id, promo_code):
    """
    Promokod qo'llash
    
    TODO:
    1. Promokod DB da borligini tekshirish
    2. Ishlatilish soni tekshirish
    3. Muddati o'tganligini tekshirish
    4. Chegirma hisoblash
    """
    # TODO: Implement
    pass