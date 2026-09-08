from models import Patient
from validators import *


def input_passport():
    while True:
        passport = input("Введите паспорт (SS SS-NNNNNN): ")

        try:
            return validate_passport(passport)
        except ValueError as error:
            print(f"Ошибка! {error}")


def input_name():
    while True:
        name = input("Введите имя: ")

        try:
            return validate_name(name)
        except ValueError as error:
            print(f"Ошибка! {error}")


def input_date():
    while True:
        value = input("Введите дату рождения (YYYY-MM-DD): ")

        try:
            return validate_date(value)
        except ValueError as error:
            print(f"Ошибка! {error}")


def input_phone():
    while True:
        phone = input("Введите телефон: ")

        try:
            return validate_phone(phone)
        except ValueError as error:
            print(f"Ошибка! {error}")


def input_temperature():
    while True:
        value = input("Введите температуру (XX.X): ")

        try:
            return validate_temperature(value)
        except ValueError as error:
            print(f"Ошибка! {error}")


def input_patient():
    return Patient(
        passport=input_passport(),
        name=input_name(),
        birth_date=input_date(),
        phone=input_phone(),
        temperature=input_temperature()
    )