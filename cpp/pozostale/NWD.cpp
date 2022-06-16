#include <iostream>
#include <vector>
using namespace std;


int nwd(int a, int b) {
    int c = 0;
    while (b != 0) {
        c = a%b;
        a = b;
        b = c;
    }
    return a;
}


int main() {
    int a;
    int b;
    cin >> a;
    cin >> b;
    cout << nwd(a, b) << "\n";
}
