"""Lokatsiya handler - Google Maps bilan"""

from config import GOOGLE_MAPS_API_KEY, CAFE_LAT, CAFE_LON

async def request_location(message):
    """
    Mijozdan lokatsiyasini so'rash
    
    TODO:
    1. Google Maps Web App ochish
    2. Yoki location button ko'rsatish
    3. Koordinatalarni saqlash
    """
    text = "📍 Iltimos, o'zingizning uyingizni tanlang yoki lokatsiyani yuboring"
    
    # TODO: KeyboardButton with request_location
    # yoki Mini App bilan Google Maps
    await message.answer(text)

async def save_location(user_id, latitude, longitude, address):
    """
    Lokatsiyani database ga saqlash
    
    TODO:
    1. User lokatsiyasini update qilish
    2. Kafe va mi joz o'rtasidagi masofani hisoblash
    """
    # TODO: Implement
    pass

def calculate_distance(lat1, lon1, lat2, lon2):
    """
    Ikki nuqta o'rtasidagi masofani hisoblash (km)
    
    TODO:
    1. Haversine formula ishlash
    """
    # TODO: Implement
    pass

async def get_map_html(latitude, longitude):
    """
    Google Maps HTML yaratish mini app uchun
    """
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Lokatsiya Tanlash</title>
        <script src="https://maps.googleapis.com/maps/api/js?key={GOOGLE_MAPS_API_KEY}"></script>
        <style>
            body {{ margin: 0; padding: 0; }}
            #map {{ height: 100vh; width: 100%; }}
        </style>
    </head>
    <body>
        <div id="map"></div>
        <script>
            // TODO: Google Maps API bilan ishlash
            // 1. Kafe lokatsiyasini ko'rsatish
            // 2. Mijoz lokatsiyasini tanlash
            // 3. Koordinatalarni bot ga yuborish
        </script>
    </body>
    </html>
    """
    return html