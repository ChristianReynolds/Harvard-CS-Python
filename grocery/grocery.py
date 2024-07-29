def getfruit(): #collect the list of fruit until controld (EOFError)
    fruits = []
    while True:
        try:                #cool idea maybe is create dict and associate a value based on count. then when someone inputs a fruit check if it exists already if it does add a value, if it doesnt add a new key
            fruits.append(str(input("")))
            pass
        except EOFError:
            break

    fruits.sort()
    return fruits

def cleanList(fruitList):
   cleanList = fruitList
   cleanList = list(set(fruitList))
   cleanList.sort()
   return cleanList


def printList(oldList,newList): #collects old and new list. using the final list count the number of times it shared .
    i = 0
    while i < len(newList):
        fruit=newList[i]
        fruitCount = oldList.count(fruit)
        fruit=fruit.upper()
        print(f"{fruitCount} {fruit}")
        i=i+1





'''def printList(oldlist):           #if 0 is the index of apple, and theres 3 apples "apple, apple, apple" with index at 0. adding + 3 (the count)

    print(oldlist)
    newlist = list(set(oldlist))
    print(newlist)

   #countn = len(oldlist);
    i = 0
    while i < len(oldlist):
        tempName = oldlist[i]
        tempNum= oldlist.count(tempName)
        print(f"{tempNum} {tempName}")
        i = 1 + (tempNum-1) '''





def main():
#gets list of fruit in aloop
#ends loop with exception
#orders and counts fruit
#prints count and then fruit in numberer ABC order
    userList=list()
    userList=getfruit()
    finalList=cleanList(userList)
    printList(userList,finalList)









main()
