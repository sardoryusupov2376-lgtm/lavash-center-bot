"""Premium handler - Lavash Premium sotish"""

from config import PREMIUM_PRICE, PREMIUM_DISCOUNT, PREMIUM_LARGE_DISCOUNT

async def show_premium_info(message):
    """
    💎 Premium info ko'rsatish
    """
    text = f"""
    💎 LAVASH PREMIUM
    
    📅 1 oy - {PREMIUM_PRICE:,} so'm
    
    ✨ PREMIUM IMKONIYATLARI:
    ✅ Har bir zakaya uchun 10% chegirma
    ✅ 300,000+ so'm da 15% chegirma
    ✅ Unlimited zakaya (cheksiz)
    ✅ Priority dastavka
    ✅ Loyalty points
    ✅ Eksklyuziv promokodlar
    ✅ Direct chat bilan admin
    
    🔥 Bugun TO'LOV QILING VA BOSHLANG!
    """
    
    # TODO: "Premium Olish" button
    await message.answer(text)

async def buy_premium(message, user_id):
    """
    Premium sotish
    
    TODO:
    1. Order yaratish (PREMIUM_PRICE summa)
    2. To'lov boshlash
    3. To'lov muvaffaqiyatli bo'lganda:
       - User.is_premium = True
       - Subscription yaratish
       - is_premium_until = today + 30 days
    """
    # TODO: Implement payment flow
    pass

async def check_premium_status(user_id):
    """
    Premium statusini tekshirish
    
    TODO:
    1. Database dan user olish
    2. premium_until tarifini tekshirish
    3. Muddati o'tgan bo'lsa, is_premium = False qilish
    """
    # TODO: Implement
    pass