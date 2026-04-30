"""Validation functions"""

import re

def validate_phone(phone):
    """
    Telefon raqamini tekshirish
    +998XXXXXXXXX format
    """
    pattern = r'^\+998\d{9}$'
    return re.match(pattern, phone) is not None

def validate_promo_code(code):
    """
    Promokod formatini tekshirish
    Masalan: LAVASH50, WELCOME10
    """
    pattern = r'^[A-Z0-9]{5,20}$'
    return re.match(pattern, code) is not None

def validate_coordinates(latitude, longitude):
    """
    Koordinatalarni tekshirish
    """
    try:
        lat = float(latitude)
        lon = float(longitude)
        return -90 <= lat <= 90 and -180 <= lon <= 180
    except:
        return False
