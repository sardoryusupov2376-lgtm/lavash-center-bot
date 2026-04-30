"""Helper functions"""

def format_price(price):
    """
    Narxni formatlash: 50000 -> "50,000 so'm"
    """
    return f"{price:,} so'm"

def format_date(date):
    """
    Sanani formatlash
    """
    return date.strftime('%d.%m.%Y %H:%M')

def get_order_status_emoji(status):
    """
    Order status uchun emoji
    """
    statuses = {
        'pending': '⏳',
        'paid': '✅',
        'preparing': '👨‍🍳',
        'delivering': '🚕',
        'completed': '✨'
    }
    return statuses.get(status, '❓')
