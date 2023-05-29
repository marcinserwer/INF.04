#include <iostream> //https://github.com/marcinserwer //Nie sprawdzone dokładnie, zrobione w 10 min na lekcji, polecam wersję w Pythonie
using namespace std;

int tab[10] = {1, 2, 5, 7, 23, 87, 56, 4, 12, 69};
int dlugosc = sizeof(tab) / sizeof(int);

void sortowanie(){
    for(int i = 0; i < dlugosc - 1; i++){
    int IndexBiezacy = i;
        for(int j = i + 1; j < dlugosc; j++)
            if(tab[j] < tab[IndexBiezacy]){
                IndexBiezacy = j;
            }
        swap(tab[IndexBiezacy], tab[i]);
  }
}

void Szuakjnajwieksza(){
    int najwieksza = tab[0];
    for(int i = 0; i < dlugosc; i++){
        if(tab[i] > najwieksza){
            najwieksza = tab[i];
        }
    }
    cout<<"Najwieksza liczba wynosi: "<<najwieksza;
}

void wyswietlanie(){
      cout << "Po sortowaniu:\n";
  for(int i = 0; i < dlugosc; i++){
      cout<<"Index "<<i<<" wynosi: "<< tab[i]<<"\n";
  }
}

int main(){
    sortowanie();
    wyswietlanie();
    Szuakjnajwieksza();
}