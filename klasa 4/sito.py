import math
tab = []


def fill(tab):
    for i in range(101):
        tab.append(True)
    tab[0] = tab[1] = False


def sito(table):

    i = 2
    while i <= round(math.sqrt(100)):
        if table[i] == True:
            for j in range(i+i, 101, i):
                table[j] = False
        i += 1

    return table


fill(tab)
sito(tab)

for i in range(100):
    if tab[i] == True:
        print(i, end=' ')
