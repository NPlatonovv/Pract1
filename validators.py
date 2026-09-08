import re
from datetime import datetime

from models import Date


def validate_passport(passport):
    if re.fullmatch(r"\d{2} \d{2}-\d{6}", passport):
        return passport

    raise ValueError("Неверный формат паспорта")


def validate_name(name):
    name = name.strip()

    if re.fullmatch(r"[А-Яа-яЁёA-Za-z]+", name):
        return name

    raise ValueError("Имя должно содержать только буквы")


def validate_date(value):
    try:
        date = datetime.strptime(value, "%Y-%m-%d")

        return Date(
            dd=date.day,
            mm=date.month,
            yyyy=date.year
        )

    except ValueError:
        raise ValueError("Неверная дата. Формат: YYYY-MM-DD")


def validate_phone(phone):
    pattern = r"\+?\d\(\d{3}\) \d{3}-\d{2}-\d{2,4}"

    if re.fullmatch(pattern, phone):
        return phone

    raise ValueError("Неверный формат телефона")


def validate_temperature(value):
    if re.fullmatch(r"\d{2}\.\d", value):
        return float(value)

    raise ValueError("Температура должна быть в формате XX.X")