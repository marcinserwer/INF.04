import os #Biblioteka do obsługi systemu operacyjnego #https://github.com/marcinserwer

class KlasaTablica: #Nazwa klasy
    def __init__(self): #Specjalna metoda konstruktora
        self.tablica = [0] * 10 #Pole klasy, które przechowuje tablicę 10 liczb całkowitych

    #/********************************************************
    #* nazwa funkcji: sortuj
    #* parametry wejściowe: "self" reprezentuje obiekt klasy "Osoba", umożliwia dostęp do zmiennych, atrybutów i metod zdefiniowanej klasy
    #* wartość zwracana: brak
    #* autor: Marcinek https://github.com/marcinserwer
    #* ****************************************************/
    def sortuj(self): #Algorytm sortowania przez wybieranie
        for i in range(len(self.tablica)): #Pętla for, która przechodzi przez każdy element w tablicy
            max_idx = i #Indeks bieżącego elementu
            for j in range(i + 1, len(self.tablica)): #Pętla for, która wybiera następną liczbę w tablicy
                if self.tablica[j] > self.tablica[max_idx]: #Sprawdza, czy wartość bieżącego elementu jest większa od poprzedniej
                    max_idx = j #Jeśli tak, to poprzednia liczba jest zmieniana na większą
            self.tablica[i], self.tablica[max_idx] = self.tablica[max_idx], self.tablica[i] #Zamienia się wartości bieżącego elementu z elementem o indeksie max_idx.
        
    #/********************************************************
    #* nazwa funkcji: __szukaj_najwyzsza
    #* parametry wejściowe: "self" reprezentuje obiekt klasy "Osoba", umożliwia dostęp do zmiennych, atrybutów i metod zdefiniowanej klasy
    #* wartość zwracana: "najwyzsza" - najwyższa wartość w tablicy
    #* autor: Marcinek https://github.com/marcinserwer
    #* ****************************************************/
    def __szukaj_najwyzsza(self): #"__"Prywatna metoda szukająca
        najwyzsza = self.tablica[0] #Wartością najwyższą jest pierwszy element tablicy
        for i in range(1, len(self.tablica)): #Pętla for, przechodzi przez resztę tablicy 
            if self.tablica[i] > najwyzsza: #Sprawdza, czy wartość bieżącej pozycji w tablicy jest większa od zmiennej "najwyzsza".
                najwyzsza = self.tablica[i] #Najwyższa liczba jest zamieniona na większą
        return najwyzsza
    
    def wypisz_posortowana(self):
        self.sortuj()
        print("Posortowana tablica:")
        for element in self.tablica:
            print(element)

    def znajdz_i_wypisz_najwyzsza(self):
        najwyzsza = self.__szukaj_najwyzsza()
        print("Najwyższa wartość w tablicy:", najwyzsza)


def wprowadz_liczby_do_tablicy(obiekt): #Nazwa klasy i argumentem jest klasa "KlasaTablica" 
    for i in range(len(obiekt.tablica)): #Pętla od 0 do 9, Czyli długość pola klasy 
        obiekt.tablica[i] = int(input(f"Wprowadź liczbę dla indeksu {i}: ")) #Umożliwia wpisywanie do tablicy liczb int z klawiatury


MojaTablica = KlasaTablica()
wprowadz_liczby_do_tablicy(MojaTablica)
MojaTablica.wypisz_posortowana()
MojaTablica.znajdz_i_wypisz_najwyzsza()