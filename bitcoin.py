import sys
import requests

l = len(sys.argv)
if l == 2:
    try:
        index = float(sys.argv[1])

    except:
        print('Please enter a number')
        sys.exit(1)
else:
    print('Something is not fine')
    sys.exit(1)


try:
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    bitcoin_price =  r.json()['bpi']['USD']['rate_float']
    amount = index * bitcoin_price
    print(f'${amount:,.4f}')
except requests.RequestException:
    print('There was an error with your request')