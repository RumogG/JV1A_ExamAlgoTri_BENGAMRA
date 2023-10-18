from random import randint

#1  ----------------------------------------------------------------------------------------------------------


myTable = [0]*10

for i in range(len(myTable)):
   myTable[i] = randint(0, 20)

print(myTable)

a = int(input("Première case ?\n")) - 1
b = int(input("Deuxième case ?\n")) - 1

stock1 = myTable[a]
myTable[a] = myTable[b]
myTable[b] = stock1

print(myTable)
