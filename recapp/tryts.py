import secrets
from string import capwords
from datetime import datetime


def generate_id(feed):
    new_code = capwords(secrets.token_hex(2))
    date_now = datetime.utcnow().date()
    date_now = str(date_now).split('-')
    date_now = f"{date_now[1]}{date_now[2]}{date_now[0][2:]}"
    generated_id = f"{feed}{new_code}-{date_now}"
    return generated_id


def greeting_tag():
    time = datetime.now().hour
    greeting = "Morning" if 5 <= time < 12 else "Afternoon" if time < 17 else "Evening"

    return greeting
