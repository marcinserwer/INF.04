import os #60 STRONA W INFORMATORZE

#********************************************************
#* nazwa funkcji: <Szyfrowanie>
#*
#* parametry wejściowe: <TekstDoZaszyfrowania> - <Przechowuje tekst który użytkownik wpisał z klawiatury>
#* wartość zwracana: <Zwraca ZaszyfrowanyTekst czyli tekst po zaszyfrowaniu>
#* opis funkcji: <Sprawdza po każdej literce czy można tą liternkę zamienić na inną, jeśli tak to zamiena, jeśli nie to zostawia na miejscu ją>
#*
#* autor: <Marcinek> https://github.com/marcinserwer
#* ****************************************************/

def Szyfrowanie(TekstDoZaszyfrowania): #Funkcja szyfrowania, która przyjmuje jako argument wprowadzony tekst
    ZaszyfrowanyTekst = ""
    for litera in TekstDoZaszyfrowania:
        if litera == "P":
            ZaszyfrowanyTekst += "O"
        elif litera == "R":
            ZaszyfrowanyTekst += "Y"
        elif litera == "O":
            ZaszyfrowanyTekst += "P"
        elif litera == "G":
            ZaszyfrowanyTekst += "A"
        elif litera == "R":
            ZaszyfrowanyTekst += "Y"
        elif litera == "A":
            ZaszyfrowanyTekst += "G"
        elif litera == "M":
            ZaszyfrowanyTekst += "M"
        else:
            ZaszyfrowanyTekst += litera
    return ZaszyfrowanyTekst #Funkcja zwraca zaszyfrowany tekst

#W programie głównym występuje wczytanie tekstu z klawiatury, a po zaszyfrowaniu wyświetlenie zaszyfrowanej jego wersji
TekstDoZaszyfrowania = input("Podaj tekst który chcesz zaszyfrować: ")
TekstPoZaszyfrowaniu = Szyfrowanie(TekstDoZaszyfrowania) 
print ("Zaszyfrowany tekst: ", TekstPoZaszyfrowaniu)