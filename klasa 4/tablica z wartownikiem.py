import random

def fill_table(table,searchNum):
    for i in range(50):
        table.append(random.randint(1,100))
        if i==49 :table[i]= searchNum;
    for i in range(50):
        print(str(i)+". " +str(table[i])+", ",end="")
    print()
        
def search_table(table,searchNum):
    for i in range(50):
        if int(searchNum)==table[i]:
            return i
        elif i==49 and table[-1]==searchNum:
            return "nie ma takiej liczby"
        
    
            
            
number_tab=[]
searching_number=input("podaj liczbę ")

fill_table(number_tab,searching_number)
print(search_table(number_tab,searching_number))