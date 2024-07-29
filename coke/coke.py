def main():
    x = 50
    while(x > 0):
        print("Amount Due: "+str(x))
        x=subtractBalance(x)

    print(f"Change Owed: {x*-1}")

def subtractBalance(balance):
    p = False
    while p == False:
        coin = int(input("Insert Coin: "))
        if coin in [5,10,25]:
            balance = balance - coin
            return (balance)
        else:
            return (balance)







main()


