import os #Biblioteka do obsługi systemu operacyjnego #https://github.com/marcinserwer
import random #Biblioteka do losowania liczb

tablica = [random.randint(1, 100) for _ in range(50)]

# ******************************************************
#  nazwa funkcji: <PrzeszukiwanieTablicyZWartownikiem>
#  argumenty: <arr> - <tablica 50 elementowa>
#             <x> - <Szukana liczba>
#  typ zwracany: <i>, <Indeks pod którym znaleziono liczbę>
#  informacje: <opis>
#  autor: <Martin https://github.com/marcinserwer>
# *****************************************************
def PrzeszukiwanieTablicyZWartownikiem(tablica, szukana):
    Dlugosc = len(tablica) #Długość tablicy
    OstatniElement = tablica[Dlugosc-1] #Ostatni element jest zapisywany do zmiennej aby później go przywołać
    tablica[Dlugosc-1] = szukana #Ostatniej komórce tablicy znajduje się szukany element x, który pełni rolę wartownika

    indeks = 0
    while tablica[indeks] != szukana: #Powoduje przejście po kolejnych elementach tablicy tablica, aż do znalezienia elementu x lub do przejścia przez wszystkie elementy tablicy
        indeks += 1 #Indeks elementu

    tablica[Dlugosc-1] = OstatniElement #przypisuje mu oryginalną wartość ostatniego elementu w tablicy, po użyciu go jako wartownika
    if indeks < Dlugosc-1 or tablica[Dlugosc-1] == szukana: #Jeśli indeks "i" jest mniejszy niż długość tablicy, lub czy wartość wartownicza xzostała znaleziona na ostatniej pozycji tablicy wejściowej 
        print("Zawartość tablicy:", tablica)
        print("Indeks, pod którym odszukano wartość:", indeks)
    else:
        print("Zawartość tablicy:", tablica)
        print("Nie znaleziono szukanego elementu")

szukana = int(input("Jaką chcesz znaleść liczbę: ")) #Umożliwia wpisywanie do tablicy liczb int z klawiatury

PrzeszukiwanieTablicyZWartownikiem(tablica, szukana)