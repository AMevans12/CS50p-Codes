from um import count

def main():
    test_cases()
    test_with_randomString()
    test_with_punc()

def test_cases():
    assert count('UM') == 1
    assert count('Um') == 1

def test_with_randomString():
    assert count('um thanks for the book') == 1
    assert count('regular um expression um') == 2

def test_with_punc():
    assert count('um?') == 1
    assert count('hello.. um, world') == 1
    assert count('um... um... um...') == 3
if __name__ == '__main__':
    main()
