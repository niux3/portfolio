from datetime import datetime
import locale


try:
    locale.setlocale(locale.LC_TIME, 'fr_FR.UTF-8')
except locale.Error:
    # Fallback si le système ne supporte pas 'fr_FR.UTF-8'
    locale.setlocale(locale.LC_TIME, '')

def format_date_fr(value, format="%d %B %Y"):
    if isinstance(value, str):
        value = datetime.fromisoformat(value)
    return value.strftime(format)
