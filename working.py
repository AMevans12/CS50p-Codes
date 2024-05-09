import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(r"^([1-9]|1[0-2])(?::)?(0[0-9]|[1-5][0-9])? (AM|PM) to ([1-9]|1[0-2])(?::)?(0[0-9]|[1-5][0-9])? (AM|PM)$",s):
        start_hour = int(matches.group(1))
        start_minutes = matches.group(2)
        start_meridiem = matches.group(3)
        finish_hour= int(matches.group(4))
        finish_minutes = matches.group(5)
        finish_meridiem = matches.group(6)

        if start_meridiem == "PM" and start_hour !=12:
            start_hour = int(start_hour)+12
        if start_meridiem == "AM" and start_hour==12:
            start_hour="00"
        if finish_meridiem == "PM" and finish_hour!=12:
            finish_hour = int(finish_hour)+12
        if finish_meridiem == "AM" and finish_hour==12:
            finish_hour=str(0)
        if start_minutes:
            return (f"{start_hour:02}:{start_minutes} to {finish_hour:02}:{finish_minutes}")
        else:
            return (f"{start_hour:02}:00 to {finish_hour:02}:00")

    else:
        raise ValueError


if __name__ == "__main__":
    main()
