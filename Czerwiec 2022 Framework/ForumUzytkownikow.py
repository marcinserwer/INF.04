import os #Biblioteka do obsługi systemu operacyjnego #https://github.com/marcinserwer

class Osoba:
    __liczba_instancji = 0
    
    def __init__(self, _id = 0, _imie = ""): #Bezparametrowy, ustawia wartości 0 i pusty dla pól 
        self.__id = _id #Ustawia id = 0
        self.__imie = _imie #Ustawia puste imię
        Osoba.__liczba_instancji += 1 #Ikrementuje liczbę instancji klasy
    
    def __init__(self, _id, _imie): #Z dwoma parametrami, które przekazują wartości id i imienia
        self.__id = _id #Przypisuje id 
        self.__imie = _imie #Przypisuje imię
        Osoba.__liczba_instancji += 1 #Ikrementuje liczbę instancji klasy

    def __init_copy__(self, osobacopy): #Kopiujący
        self.__id = osobacopy.__id
        self.__imie = osobacopy.__imie
        Osoba.__liczba_instancji += 1
    
    def wypisz_imie(self, argument):
        if self.__imie == '': #Jeśli jest puste imię
            print("Brak danych")
        else:
            print("Cześć ",argument,", mam na imię ",self.__imie)
    
    @staticmethod
    def liczba_instancji(): #Publiczna statyczne liczba_instancji
        return Osoba.__liczba_instancji


#Testy utworzonej aplikacji

licznik = Osoba.liczba_instancji() #Wyświetlenie komunikatu „Liczba zarejestrowanych osób to <licznik>”, gdzie <licznik> jest wartością pobraną z pola statycznego klasy
print("Liczba zarejestrowanych osób to", licznik)

osoba0 = Osoba(0, "") #Utworzenie obiektu za pomocą konstruktora bezparametrowego. (w Python konstruktor z parametrami, których wartości domyślne to: 0 i "" lub null)

#Utworzenie obiektu za pomocą konstruktora z dwoma parametrami. Dane obiektu wprowadzane z klawiatury.
id = int(input("Podaj ID osoby: "))
imie = input("Podaj imię osoby: ")
osoba1 = Osoba(id, imie)

osoba2 = Osoba(1, "Marcinek") #Przekazujący
osoba2.wypisz_imie("Paulina") #Wypisujący
osoba3 = osoba2 #Utworzenie obiektu za pomocą konstruktora kopiującego

for osoba in [osoba1, osoba2, osoba3]: #Wywołanie metody do wypisania imienia z parametrem wejściowym równym „Jan” dla wszystkich utworzonych obiektów
    osoba.wypisz_imie("Jan")

licznik = Osoba.liczba_instancji() #Ponowne wyświetlenie komunikatu „Liczba zarejestrowanych osób to <licznik>”, gdzie <licznik> jest wartością pobraną z pola statycznego klasy
print("Liczba zarejestrowanych osób to", licznik)