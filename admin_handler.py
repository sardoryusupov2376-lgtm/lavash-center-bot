"""Admin handler - Admin panel"""

from config import ADMIN_ID

async def admin_panel(message):
    """
    /admin - Admin panel
    
    TODO:
    1. Admin tekshirish
    2. Quyidagi variantlarni ko'rsatish:
       - Statistika
       - Taomlarni qo'shish/o'chirish
       - Promokodlarni qo'shish
       - Broadcast (xabar yuborish)
       - Buyurtmalarni kuzatish
    """
    if message.from_user.id != ADMIN_ID:
        await message.answer("❌ Siz admin emassiz")
        return
    
    text = """
    ⚙️ ADMIN PANEL
    
    1️⃣ Statistika
    2️⃣ Taomlar
    3️⃣ Promokodlar
    4️⃣ Xabar yuborish
    5️⃣ Buyurtmalar
    """
    
    # TODO: Inline buttons
    await message.answer(text)

async def add_product(admin_id, category, name, price, image_url=None):
    """
    Taom qo'shish
    
    TODO:
    1. Product database ga saqlash
    2. Admin ga tasdiqlash
    """
    # TODO: Implement
    pass

async def add_promo_code(admin_id, code, discount_percent, expires_at=None):
    """
    Promokod qo'shish
    
    TODO:
    1. PromoCode database ga saqlash
    2. Admin ga tasdiqlash
    """
    # TODO: Implement
    pass

async def broadcast_message(admin_id, text):
    """
    Xabar yuborish (barcha userlarga)
    
    TODO:
    1. Barcha users ni olish
    2. Har biriga xabar yuborish
    3. Yuborilgan soni ko'rsatish
    """
    # TODO: Implement
    pass