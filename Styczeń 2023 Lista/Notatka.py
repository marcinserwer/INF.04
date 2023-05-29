import os #https://github.com/marcinserwer

#************************************************
# klasa: <Notatka>
# opis: <Klasa przechowuje, wyśweitla notaki i zlicza ich ilość>
# pola: <LicznikNotatek - Liczbę notatek>
#       <Id - Id notatki>
#       <Tytul - Tytuł notatki który użytkownik poda>
#       <TrescNotatki - Treść notatki który użytkownik poda>
# autor: <Marcinek https://github.com/marcinserwer >
#************************************************

class Notatka:
    __LicznikNotatek = 0 #Statyczne numeryczne licznika notatek do zliczania utworzonych notatek (nie są dostępne dla klas potomnych)
    __Id = 0 #Numeryczne do zapisu unikalnego identyfikatora (nie są dostępne dla klas potomnych)
    _Tytul = "" #Tekstowe do zapisu tytułu notatki (są dostępne dla klas potomnych)
    _TrescNotatki = "" #Tekstowe do zapisu treści notatki (są dostępne dla klas potomnych)

    def __init__(self, Tytul, TrescNotatki): #Konstruktor o parametrach wejściowych dla tytułu i treści
        Notatka.__LicznikNotatek += 1 #Inkrementuje licznik notatek 
        Notatka.__Id = self.__LicznikNotatek #Ustawia pole identyfikatora równe licznikowi notatek
        Notatka._Tytul = Tytul #Ustawia pole tytułu równe parametrowi
        Notatka._TrescNotatki = TrescNotatki #Ustawia pole treść równe parametrowi

    def WyswietlNotatke(self): #Metoda bezparametrowe i niezwracająca wartości, wyświetlenia tytułu i treści notatki 
        print(self._Tytul," ", self._TrescNotatki)
    
    def Diagnostyka(self): #Metoda bezparametrowe i niezwracająca wartości, diagnostyczna wypisująca zawartości wszystkich pól oddzielone od siebie średnikami
        print(self.__LicznikNotatek,", ",self.__Id,", ",self._Tytul,", ", self._TrescNotatki)

Tytul = input("Podaj tytuł notatki: ")
Tresc = input("Podaj treść notatki: ")

notatka1 = Notatka(Tytul, Tresc)
notatka1.WyswietlNotatke()
notatka1.Diagnostyka()

notatka2 = Notatka("Zakupy", "Kwiaty, truskawki")
notatka2.WyswietlNotatke()
notatka2.Diagnostyka()