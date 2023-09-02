from datetime import datetime

from faker import Faker

fake = Faker()


def fake_int_id(max_value: int = 100000) -> int:
    return fake.pyint(0, max_value)


def fake_name() -> str:
    return fake.name()


def fake_email(name: str) -> str:
    name_part = ".".join(name.split(" "))
    return f"{name_part}@{fake.domain_name()}"


def fake_phone() -> str:
    return fake.phone_number()


def fake_datetime() -> datetime:
    return fake.date_time()
