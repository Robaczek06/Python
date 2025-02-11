class Osoba:
    liczba_osób = 0

    def __init__(self, id=0, imie=""):
        self.__id = id
        self.__imie = imie
        Osoba.liczba_osób += 1

    def copy(self):
        return Osoba(self.__id, self.__imie)

    def hello(self, argument):
        if self.__imie:
            print(f"Cześć {argument}, mam na imię {self.__imie}")
        else:
            print("Brak danych")


osoba1 = Osoba()
osoba2 = Osoba(3, "Mateusz")
osoba3 = Osoba.copy(osoba2)

osoba1.hello("Ola")
osoba2.hello("Ola")
osoba3.hello("Ola")

print(f"Liczba instancji klasy Osoba: {Osoba.liczba_osób}")
