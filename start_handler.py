"""START komandasi handler"""

async def start_command(message):
    """
    /start - Foydalanuvchini khush kelibsiz qiling
    
    TODO:
    1. User DB ga qo'shish yoki update qilish
    2. Asosiy menu buttons ko'rsatish
    3. Premium status tekshirish
    """
    user_id = message.from_user.id
    full_name = message.from_user.full_name
    
    # TODO: Database bilan ishlash
    # user = User.get_or_create(user_id, full_name)
    
    text = f"""
    ✅ Salom, {full_name}!
    
    🍕 Lavash Center ga khush kelibsiz!
    
    Quyidagi buyruqlarni ishlata olasiz:
    📋 /menu - Menyu ko'rish
    🛒 /cart - Savat
    💎 /premium - Premium olish
    👤 /profile - Profil
    ⚙️ /help - Yordam
    """
    
    # TODO: Inline buttons yaratish
    # buttons = [
    #     [InlineKeyboardButton(text="📋 Menyu", callback_data="menu")],
    #     [InlineKeyboardButton(text="💎 Premium", callback_data="premium")],
    # ]
    
    await message.answer(text)

async def help_command(message):
    """
    /help - Yordam
    """
    text = """
    🆘 YORDAM
    
    ❓ Savollar:
    1. Menyu qanday ko'rish? → /menu
    2. Premium qanday olish? → /premium
    3. Zakaya qanday qilish? → /menu
    
    📞 Muammolar:
    Agar muammo bo'lsa, admin bilan bog'lanish:
    👉 @admin_username
    """
    await message.answer(text)