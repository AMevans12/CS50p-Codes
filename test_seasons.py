import pytest
from datetime import datetime
from io import StringIO
from contextlib import redirect_stdout
from asg import get_time

# Valid input test cases
@pytest.mark.parametrize("input_date, expected_output", [
    ("2023-04-23", "One year, fifty-one weeks, six days minutes"),
    ("2022-04-23", "One year, fifty-two weeks, six days minutes"),
    ("2000-01-01", "Eight hundred fifty-four thousand, one hundred forty-four minutes")  # Leap year
])
def test_valid_input(input_date, expected_output):
    with redirect_stdout(StringIO()) as output:
        get_time(input_date)
        assert output.getvalue().strip() == expected_output

# Invalid input test cases
@pytest.mark.parametrize("input_date", [
    "2023/04/23",  # Incorrect date format
    "2023-13-01",  # Invalid month
    "2023-04-32",  # Invalid day
    "2023-02-29",  # Invalid date for non-leap year
    "hello",       # Invalid string
    ""             # Empty input
])
def test_invalid_input(input_date):
    with pytest.raises(SystemExit):
        get_time(input_date)

# Boundary cases
def test_boundary_case():
    # Testing with the current date, should output 0 minutes
    current_date = datetime.now().strftime("%Y-%m-%d")
    with redirect_stdout(StringIO()) as output:
        get_time(current_date)
        assert output.getvalue().strip() == "Zero minutes"

    # Testing with a very old date, should output a large number of minutes
    very_old_date = "1900-01-01"
    expected_output = "Thirty-nine million, three hundred twenty-eight thousand, eight hundred minutes"
    with redirect_stdout(StringIO()) as output:
        get_time(very_old_date)
        assert output.getvalue().strip() == expected_output

if __name__ == "__main__":
    pytest.main()
