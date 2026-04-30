"""To'lov handler - Click, Payme"""

from config import (
    CLICK_MERCHANT_ID,
    CLICK_SERVICE_ID,
    PAYME_MERCHANT_ID
)

class ClickPayment:
    """Click API integratsiyasi"""
    
    def __init__(self):
        self.merchant_id = CLICK_MERCHANT_ID
        self.service_id = CLICK_SERVICE_ID
    
    async def create_invoice(self, order_id, amount):
        """
        Click invoice yaratish
        
        TODO:
        1. Click API ga so'rov yuborish
        2. Invoice ID olish
        3. To'lov linkini yaratish
        """
        # https://click.uz/api/...
        pass
    
    async def verify_payment(self, transaction_id):
        """
        To'lovni tekshirish
        """
        # TODO: Implement
        pass

class PaymePayment:
    """Payme API integratsiyasi"""
    
    def __init__(self):
        self.merchant_id = PAYME_MERCHANT_ID
    
    async def create_invoice(self, order_id, amount):
        """
        Payme invoice yaratish
        
        TODO:
        1. Payme API ga so'rov yuborish
        2. Invoice ID olish
        """
        pass
    
    async def verify_payment(self, transaction_id):
        """
        To'lovni tekshirish
        """
        # TODO: Implement
        pass

async def payment_callback(request):
    """
    Click/Payme callback - To'lov muvaffaqiyatli bo'lganda
    
    TODO:
    1. Callback signaturni tekshirish
    2. Order statusini 'paid' qilish
    3. Admin ga xabar berish
    4. User ga xabar berish
    """
    # TODO: Implement
    pass

async def show_payment_methods(message, total_price):
    """
    To'lov usullarini ko'rsatish
    
    - 💳 Click
    - 💳 Payme
    - 💵 Naqd (dastavkada)
    """
    # TODO: Implement with inline buttons
    pass