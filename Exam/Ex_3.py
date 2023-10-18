from random import randint

#3  ----------------------------------------------------------------------------------------------------------


def fonction_indice (myTable, indice_depart):

    min = myTable[indice_depart]
    indice = indice_depart

    for i in range((indice_depart - 1), -1, -1):
         if (min<myTable[i]):
            indice = i

    return indice

def fonction_pop (myTable, indice_val_min, indice_depart):
    stock1 = myTable.pop(indice_depart)
    myTable.insert(indice_val_min, stock1)

    return myTable



myTable = [0]*10

for i in range(len(myTable)):
    myTable[i] = randint(0, 20)

print(myTable)

for i in range(len(myTable)):
    indice_min = fonction_indice(myTable, i)
    myTable = fonction_pop(myTable, indice_min, i)


print(myTable)
