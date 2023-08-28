#include <iostream>

using namespace std;

long long maks_il_cukierkow(int *cukierki, int il_domow) {
    long long wynik = 0;
    int suma = 0;
    for (int i = il_domow - 1; i >= 0; i--) {
        if (cukierki[i] % 2 == 1) {
            suma = il_domow - i - 1 - suma;

        } else {
            suma = suma + 1;
        }
        wynik = wynik + suma;
    }
    return wynik;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int il_domow;
    cin >> il_domow;
    int cukierki[il_domow];
    for (int &liczba : cukierki) {
        cin >> liczba;
    }
    cout << maks_il_cukierkow(cukierki, il_domow) << "\n";
}
