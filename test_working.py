from working import convert
import pytest

def main():
    test_formatting()
    test_time()
    test_wrong_minutes()
    test_wrong_hours

def test_formatting():
     with pytest.raises(ValueError):
         convert('9 AM - 5 PM')

def test_wrong_minutes():
    with pytest.raises(ValueError):
        convert('9:60 AM to 9:60 PM')

def test_wrong_hours():
    with pytest.raises(ValueError):
        convert('13 PM to 17 PM')

def test_time():
    assert convert('9:00 AM to 5:00 PM') == '09:00 to 17:00'
    assert convert('10:30 PM to 8:50 AM') == '22:30 to 08:50'

if __name__ == '__main__':
    main()
