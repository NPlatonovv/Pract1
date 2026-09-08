import unittest

from validators import *
from models import Date


class TestValidatePassport(unittest.TestCase):

    def test_valid_passport(self):
        result = validate_passport("12 34-567890")

        self.assertEqual(result, "12 34-567890")

    def test_invalid_passport(self):
        with self.assertRaises(ValueError):
            validate_passport("123456")


class TestValidateName(unittest.TestCase):

    def test_valid_name(self):
        result = validate_name("Никита")

        self.assertEqual(result, "Никита")

    def test_invalid_name(self):
        with self.assertRaises(ValueError):
            validate_name("123")

    def test_name_with_spaces(self):
        result = validate_name("  Никита  ")

        self.assertEqual(result, "Никита")


class TestValidateDate(unittest.TestCase):

    def test_valid_date(self):
        result = validate_date("2005-12-25")

        self.assertEqual(result, Date(25, 12, 2005))

    def test_invalid_date(self):
        with self.assertRaises(ValueError):
            validate_date("2005-02-30")

    def test_invalid_date_format(self):
        with self.assertRaises(ValueError):
            validate_date("25.12.2005")


class TestValidatePhone(unittest.TestCase):

    def test_valid_phone_with_plus(self):
        result = validate_phone("+7(999) 123-45-67")

        self.assertEqual(result, "+7(999) 123-45-67")

    def test_valid_phone_without_plus(self):
        result = validate_phone("7(999) 123-45-67")

        self.assertEqual(result, "7(999) 123-45-67")

    def test_invalid_phone(self):
        with self.assertRaises(ValueError):
            validate_phone("89991234567")


class TestValidateTemperature(unittest.TestCase):

    def test_valid_temperature(self):
        result = validate_temperature("36.6")

        self.assertEqual(result, 36.6)

    def test_valid_temperature_zero(self):
        result = validate_temperature("00.0")

        self.assertEqual(result, 0.0)

    def test_invalid_temperature_without_decimal(self):
        with self.assertRaises(ValueError):
            validate_temperature("36")

    def test_invalid_temperature_with_comma(self):
        with self.assertRaises(ValueError):
            validate_temperature("36,6")

    def test_invalid_temperature_wrong_format(self):
        with self.assertRaises(ValueError):
            validate_temperature("100.0")


if __name__ == "__main__":
    unittest.main()