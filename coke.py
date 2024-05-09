amount = 50

while amount>0:

    print("Amount Due: ",amount)
    coin = int(input("Insert Coin: "))
    if coin in [25,10,5]:

     amount = amount-coin


change = abs(amount)
print("Change Owed: ",change)


