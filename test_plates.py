from plates import is_valid

def main():
    test_numberofCharacter()
    test_startwithLetters()
    test_middleNumbers()
    test_zero()
    test_punctuation()

def test_numberofCharacter():
    assert is_valid('vc') == True
    assert is_valid('50') == False
    assert is_valid('points') == True
    assert is_valid('MynaemisKhan') == False
    assert is_valid('x') == False

def test_startwithLetters():
    assert is_valid('MCst69') == True
    assert is_valid('69MCst') == False
    assert is_valid('Ab21') == True

def test_middleNumbers():
    assert is_valid('AAA22A') == False
    assert is_valid('cs501') == True

def test_zero():
    assert is_valid('po09') == False
    assert is_valid('CS50') == True

def test_punctuation():
    assert is_valid('cs!22') == False
    assert is_valid('cs 22') == False
    assert is_valid('cs22') == True

if __name__ == '__main__':
    main()
