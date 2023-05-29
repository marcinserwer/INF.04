import os #Biblioteka do obsługi systemu operacyjnego #https://github.com/marcinserwer

#**********************************************
#nazwa funkcji: <SzukajNWD>
#opis funkcji: <Szuka najawiększy wspólny dzielnik>
#parametry: <LiczbaA – Liczba pierwsza którą użytkownik wpisuje
# LiczbaB – Liczba druga którą użytkownik wpisuje>
#zwracany typ i opis: <Zwraca liczbę całkowitą - wspólny dzielnik>
#autor: <Marcinek https://github.com/marcinserwer >
#***********************************************

def SzukajNWD(LiczbaA, LiczbaB):
    while(LiczbaA != LiczbaB): #Pętla wykonuje się dopóki LiczbaA nie jest równa LiczbaB
        if(LiczbaA > LiczbaB): #Sprawdzanie, czy LiczbaA jest większa od LiczbaB
            LiczbaA = LiczbaA - LiczbaB #Odejmowanie LiczbaB od LiczbaA
        else:
            LiczbaB = LiczbaB - LiczbaA # Odejmowanie LiczbaA od LiczbaB
    else:
        return LiczbaA
    
LiczbaA = int(input("Podaj liczbę A: ")) #Wprowadzanie z klawiatury liczby dla  LiczbaA
LiczbaB = int(input("Podaj liczbę B: ")) #Wprowadzanie z klawiatury liczby dla  LiczbaB

print("NWD wynosi:", SzukajNWD(LiczbaA, LiczbaB)); #Wyświetlanie wyniku NWD
