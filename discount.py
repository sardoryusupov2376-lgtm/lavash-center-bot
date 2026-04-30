"""Chegirma hisoblash logikasi"""

from config import (
    PREMIUM_DISCOUNT,
    PREMIUM_LARGE_DISCOUNT,
    FREE_DISCOUNT,
    FREE_LIMIT_ORDERS
)

def calculate_free_user_discount(user, total_price):
    """
    Free user uchun chegirma
    - 1-3 zakaya: 1 marta 10%
    - 4+ zakaya: chegirma yo'q
    """
    if user.total_orders >= FREE_LIMIT_ORDERS:
        return 0
    
    if user.free_discount_used:
        return 0
    
    return int(FREE_DISCOUNT * 100)  # 10%

def calculate_premium_user_discount(total_price):
    """
    Premium user uchun chegirma
    - Default: 10%
    - 300,000+: 15%
    """
    if total_price >= 300000:
        return int(PREMIUM_LARGE_DISCOUNT * 100)  # 15%
    
    return int(PREMIUM_DISCOUNT * 100)  # 10%

def apply_promo_code(promo_code_obj, total_price):
    """
    Promokod qo'llash
    """
    if not promo_code_obj.is_active:
        return None
    
    if promo_code_obj.max_uses and promo_code_obj.used_count >= promo_code_obj.max_uses:
        return None
    
    # TODO: expires_at tekshirish
    
    return promo_code_obj.discount_percent

def calculate_final_price(total_price, discount_percent, promo_discount=0):
    """
    Final narx hisoblash
    """
    # Discount qo'shish
    total_discount = discount_percent + promo_discount
    
    # Maximum 100% bo'lmasin
    if total_discount > 100:
        total_discount = 100
    
    discount_amount = total_price * (total_discount / 100)
    final_price = total_price - discount_amount
    
    return {
        'discount_percent': total_discount,
        'discount_amount': discount_amount,
        'final_price': final_price
    }
