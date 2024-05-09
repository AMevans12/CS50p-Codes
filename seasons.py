import sys
import re
from datetime import datetime, date
import inflect

number_to_words = inflect.engine()  

class Birthdate:
    def __init__(self, date_str):
        self.date_str = date_str

    def __str__(self):
        return f"{self.date_str}"

    @classmethod
    def get_date(cls):
        birth_input = input("Enter your birth date (YYYY-MM-DD): ")
        date_string = birth_input
        if date_string := re.search(r"^([0-9]{4})\-([0-9]{2})\-([0-9]{2})$", date_string):
            year = int(date_string.group(1))
            month = int(date_string.group(2))
            day = int(date_string.group(3))
            if month <= 12 and day <= 31:
                birth_date = date(year, month, day)
                return birth_date
            else:
                sys.exit("Invalid date format")
        else:
            sys.exit("Invalid date format")

class CurrentDate:
    def __init__(self, current_date):
        self.current_date = current_date

    def __str__(self):
        return f"{self.current_date}"

    @classmethod
    def get_date(cls):
        current_date = date.today()
        return current_date

def main():
    birth_date_obj = Birthdate.get_date()
    current_date_obj = CurrentDate.get_date()
    age_in_days = current_date_obj - birth_date_obj
    age_in_minutes = age_in_days.days * 1440
    words = number_to_words.number_to_words(age_in_minutes, andword="")
    print(f"{words.capitalize()} minutes")

if __name__ == "__main__":
    main()
