from fuel import gauge , convert

def main():
    test_extremes()
    test_correctOutput()
    test_value_error()
    test_zero_division_error

def test_extremes():
    assert gauge(1) == 'E'
    assert gauge(99) == 'F'
    assert gauge(100) == 'F'
    assert gauge(0) == 'E'

def test_correctOutput():
    assert convert('50/100') == 50 and gauge(50) == '50%'
    assert convert('21/21') == 100 and gauge(100) == 'F'
    assert convert('21/2100') == 1 and gauge(1) == 'E'

def test_value_error():
    try:
        convert('21/e')
    except ValueError:
        pass
    else:
        assert False, "Something went wrong, Try again"

def test_zero_division_error():
    try:
        convert('100/0')
    except ZeroDivisionError:
        pass
    else:
        assert False, "Something went wrong, Try again"

if __name__ == '__main__':
    main()