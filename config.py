import os
from dotenv import load_dotenv

load_dotenv()

# Bot
BOT_TOKEN = os.getenv('BOT_TOKEN')
ADMIN_ID = int(os.getenv('ADMIN_ID', 0))

# Database
DATABASE_URL = os.getenv('DATABASE_URL')

# Payment
CLICK_MERCHANT_ID = os.getenv('CLICK_MERCHANT_ID')
CLICK_SERVICE_ID = os.getenv('CLICK_SERVICE_ID')
CLICK_SECRET_KEY = os.getenv('CLICK_SECRET_KEY')

PAYME_MERCHANT_ID = os.getenv('PAYME_MERCHANT_ID')
PAYME_SECRET_KEY = os.getenv('PAYME_SECRET_KEY')

# Maps
GOOGLE_MAPS_API_KEY = os.getenv('GOOGLE_MAPS_API_KEY')

# Taxi
UBER_API_KEY = os.getenv('UBER_API_KEY')
YANDEX_API_KEY = os.getenv('YANDEX_API_KEY')

# Cafe
CAFE_LAT = float(os.getenv('CAFE_LAT', 41.2995))
CAFE_LON = float(os.getenv('CAFE_LON', 69.2401))
CAFE_NAME = os.getenv('CAFE_NAME', 'Lavash Center')
CAFE_ADDRESS = os.getenv('CAFE_ADDRESS', 'Tashkent')

# Premium
PREMIUM_PRICE = 50000  # 50,000 som
PREMIUM_DISCOUNT = 0.10  # 10%
PREMIUM_LARGE_DISCOUNT = 0.15  # 15% (300,000+)
FREE_LIMIT_ORDERS = 3
FREE_DISCOUNT = 0.10  # 1 marta

# Taxi IDs
TAXI_UBER = 1266
TAXI_YANDEX = 1228