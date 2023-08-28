#include <iostream>
#include <string>
#include <vector>
#include <map>
using namespace std;

vector<string> gesty{"kamień", "papier", "nożyce"};
map<string, string> wygrywa = {
    {"kamień", "nożyce"},
    {"papier", "kamień"},
    {"nożyce", "papier"}
};

string wybor_komputera() {
    return "kamień";
}


void gra() {
    string gracz;
    string komputer;
    int do_ilu;
    int wynik_gracza = 0;
    int wynik_komputera = 0;
    cout << "Do ilu chcesz grać?\n";
    cin >> do_ilu;
    while (wynik_gracza != do_ilu and wynik_komputera != do_ilu) {
        cin >> gracz;
        if ((find(gesty.begin(), gesty.end(), gracz) == gesty.end())) {
            cout << "\nNie ma takiego gestu! Możesz podać tylko kamień, nożyce lub papier.\n";
        }
        else {
            komputer = wybor_komputera();
            if (wygrywa[komputer] == gracz) {
                wynik_komputera += 1;
                cout << "\nPunkt dla komputera!\n";
            }
            else if (wygrywa[gracz] == komputer) {
                wynik_gracza += 1;
                cout << "\nPunkt dla gracza!\n";
            }
            else {
                cout << "\nRemis!\n";
            }
            cout << "Wynik gracza: " << wynik_gracza << "\n";
            cout << "Wynik komputera: " << wynik_komputera << "\n\n";
        }
    }
    if (wynik_gracza == do_ilu) {
        cout << "Wygrywa gracz!\n";
    }
    else {
        cout << "Wygrywa komputer!\n";
    }
}


int main() {
    gra();
}
