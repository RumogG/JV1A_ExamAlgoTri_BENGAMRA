from random import randint

#2  ----------------------------------------------------------------------------------------------------------


myTable = [0]*10

for i in range(len(myTable)):
    myTable[i] = randint(0, 20)

print(myTable)

for i in range(len(myTable)):
    while (myTable[i-1] > myTable[i]):
        stock1 = myTable[i-1]
        myTable[i-1] = myTable[i]
        myTable[i] = stock1
        print(myTable)

print(myTable)