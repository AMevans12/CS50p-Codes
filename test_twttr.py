from twttr import shorten

def main():
    test_alpha_case()
    test_numeric()
    test_punc()

def test_alpha_case():
    assert shorten('TWITTER') == 'TWTTR'
    assert shorten('twitter') == 'twttr'
    assert shorten('TwItter') == 'Twttr'

def test_numeric():
    assert shorten('12345') == '12345'

def test_punc():
    assert shorten('.,?/!') == '.,?/!'

if __name__ == '__main__':
    main()