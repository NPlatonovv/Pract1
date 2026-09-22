import re
from datetime import datetime

from models import Date, RGB


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

    raise ValueError("Температура должна быть в формате XX.X: ")

def validate_texture(rgb):
    pattern = r"(\d{1,3}),\s?(\d{1,3}),\s?(\d{1,3})"
    match = re.fullmatch(pattern, rgb)

    if not match:
        raise ValueError("Цвет должен быть в формате XXX, XXX, XXX")

    r, g, b = (int(x) for x in match.groups())

    if not all(0 <= c <= 255 for c in (r, g, b)):
        raise ValueError("Каждое значение RGB должно быть в диапазоне 0-255")

    return RGB(R=r, G=g, B=b)