from bank import value

def main():
    test_zero()
    test_20()
    test_100()


def test_zero():
    assert value('hello') == 0
    assert value('Hello') == 0


def test_20():
    assert value('Hi how are you') == 20
    assert value('hey whassup ') == 20
    assert value('hayomotoJR') == 20


def test_100():
    assert value("What's up") == 100
    assert value('noboddycaresforcs50') == 100

if __name__ == '__main__':
    main()
