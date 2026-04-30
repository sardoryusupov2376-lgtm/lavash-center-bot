"""Menyu handler - Kategoriyalar va taomlar"""

# KATEGORIYALAR:
# 1. Lavash (Oddiy, Yog'li, Spicy)
# 2. Burger (Hamburger, Cheeseburger, Xorazm, Hot Dog)
# 3. Donar (Oddiy, Dvoynoj)
# 4. Ichimliklar (Cola, Fanta, Choy)
# 5. Fri (Kichik, Katta)

MENU_ITEMS = {
    'lavash': [
        {'id': 1, 'name': 'Lavash oddiy', 'price': 15000},
        {'id': 2, 'name': 'Lavash yog\'li', 'price': 17000},
        {'id': 3, 'name': 'Lavash spicy', 'price': 18000},
    ],
    'burger': [
        {'id': 4, 'name': 'Hamburger', 'price': 20000},
        {'id': 5, 'name': 'Cheeseburger', 'price': 22000},
        {'id': 6, 'name': 'Xorazm', 'price': 25000},
        {'id': 7, 'name': 'Hot Dog', 'price': 18000},
    ],
    'donar': [
        {'id': 8, 'name': 'Donar oddiy', 'price': 25000},
        {'id': 9, 'name': 'Donar dvoynoj', 'price': 35000},
    ],
    'drink': [
        {'id': 10, 'name': 'Cola', 'price': 5000},
        {'id': 11, 'name': 'Fanta', 'price': 5000},
        {'id': 12, 'name': 'Choy', 'price': 3000},
    ],
    'fri': [
        {'id': 13, 'name': 'Fri kichik', 'price': 12000},
        {'id': 14, 'name': 'Fri katta', 'price': 18000},
    ]
}

async def show_menu(message):
    """
    /menu - Barcha kategoriyalarni ko'rsatish
    
    TODO:
    1. Kategoriyalar uchun inline buttons yaratish
    2. Har bir kategoriyani database dan olish
    """
    text = "📋 MENYU - Kategoriya tanlang:"
    
    # TODO: Inline buttons
    # buttons = [
    #     [InlineKeyboardButton(text="🌯 Lavash", callback_data="category_lavash")],
    #     [InlineKeyboardButton(text="🍔 Burger", callback_data="category_burger")],
    #     ...
    # ]
    
    await message.answer(text)

async def show_category(callback_query, category):
    """
    Kategoriya tanlanganda taomlarni ko'rsatish
    
    TODO:
    1. Kategoriyaning barcha taomlarini ko'rsatish
    2. Rasmlarini qo'shish
    3. "Savatga qo'shish" button
    """
    items = MENU_ITEMS.get(category, [])
    
    text = f"🍽️ {category.upper()}\n\n"
    for item in items:
        text += f"🔹 {item['name']} - {item['price']:,} so'm\n"
    
    await callback_query.message.edit_text(text)