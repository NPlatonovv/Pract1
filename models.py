from dataclasses import dataclass

@dataclass
class Date:
    dd: int
    mm: int
    yyyy: int

@dataclass
class Patient:
    passport: str
    name: str
    birth_date: Date
    phone:  str
    temperature: float