#include <iostream>
#include <stdlib.h>
using namespace std;


int main() {
	int liczba = rand() % 1000000000000 + 1;
    int strzal;
    cout << "Zgadnij liczbę od 1 do 1000000000000: ";
    while (strzal != liczba){
        cin >> strzal;
        if (strzal < liczba){
            cout << "Za mało!\nSpróbuj jeszcze raz: ";
        }
        if (strzal > liczba){
            cout << "Za dużo!\nSpróbuj jeszcze raz: ";
        }
    }
    cout << "Zgadłeś!\n";
}
