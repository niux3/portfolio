import locale
from random import randint
from datetime import datetime


try:
    locale.setlocale(locale.LC_TIME, 'fr_FR.UTF-8')
except locale.Error:
    # Fallback si le système ne supporte pas 'fr_FR.UTF-8'
    locale.setlocale(locale.LC_TIME, '')

def format_date_fr(value, format="%d %B %Y"):
    if isinstance(value, str):
        value = datetime.fromisoformat(value)
    return value.strftime(format)

def random_delay_transition(value, start=1, end=100):
    return f'{value}{randint(start, end)}'
