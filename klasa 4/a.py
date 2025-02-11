def Euklides(a,b):
        while a!=b:
            if a>b:
                a=a-b
            else:
                b=b-a
        return a


a=int(input("wprowadź a: "))
b=int(input("wprowadź b: "))
if a<1 or b<1:
    print("złe wartości")
else:
    print(Euklides(a,b))

