"""Dastavka handler - Taxi tanlash"""

from config import TAXI_UBER, TAXI_YANDEX

TAXI_OPTIONS = {
    TAXI_UBER: {
        'name': 'Uber',
        'emoji': '🚗',
        'deep_link': 'uber://',
        'web_link': 'https://m.uber.com'
    },
    TAXI_YANDEX: {
        'name': 'Yandex Taxi',
        'emoji': '🚕',
        'deep_link': 'yandextaxi://',
        'web_link': 'https://taxi.yandex.com'
    }
}

async def show_delivery_options(message, cafe_lat, cafe_lon, delivery_lat, delivery_lon):
    """
    Dastavka variantlarini ko'rsatish
    
    TODO:
    1. Masofani hisoblash
    2. Taxmin vaqtni ko'rsatish
    3. Taxi applarni tanlab berish
    """
    text = f"""
    🚕 DASTAVKA VARIANTLARI:
    
    {TAXI_OPTIONS[TAXI_UBER]['emoji']} {TAXI_OPTIONS[TAXI_UBER]['name']}
    {TAXI_OPTIONS[TAXI_YANDEX]['emoji']} {TAXI_OPTIONS[TAXI_YANDEX]['name']}
    
    Birini tanlang:
    """
    
    # TODO: Inline buttons with callback_data
    await message.answer(text)

async def create_taxi_order(taxi_type, from_lat, from_lon, to_lat, to_lon, description):
    """
    Taxi buyurtmasini yaratish
    
    TODO:
    1. Taxi API ga so'rov yuborish (agar API bo'lsa)
    2. Deep link yaratish (latitude, longitude bilan)
    3. User ga taxsi app ochish
    """
    
    if taxi_type == TAXI_UBER:
        # Uber deep link
        link = f"uber://?action=setPickupLocation&pickup[latitude]={from_lat}&pickup[longitude]={from_lon}&dropoff[latitude]={to_lat}&dropoff[longitude]={to_lon}"
    
    elif taxi_type == TAXI_YANDEX:
        # Yandex Taxi deep link
        link = f"yandextaxi://route?startlocation={from_lat},{from_lon}&endlocation={to_lat},{to_lon}"
    
    return link

async def handle_taxi_selection(callback_query, taxi_type, order_id):
    """
    Taxi tanlanganda
    
    TODO:
    1. Order ma'lumotlarini olish
    2. Taxi link yaratish
    3. User ga xabar berish
    4. Taxi appni ochish
    """
    # TODO: Implement
    pass