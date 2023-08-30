from dataclasses import dataclass
from datetime import datetime


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    mobile: str
    date_of_birth_day: int
    date_of_birth_month: int
    date_of_birth_year: int
    subjects: list
    hobbies: list
    picture: str
    current_address: str
    state: str
    city: str

    def get_full_birth_date(self):
        full_birth_date = datetime(self.date_of_birth_year, self.date_of_birth_month, self.date_of_birth_day)
        return full_birth_date.strftime("%d %B,%Y")
