#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

vector<long long> byly;
long long n, x, i = 1;

long long sum_of_digits(long long input) {
    long long total = input % 10;
    while ((input /= 10) != 0) total += input % 10;
    return total;
}

long long podaj_n_ciagu() {
    vector<long long>::iterator it;
    while (n - i) {
        byly.push_back(x);
        x = sum_of_digits(x) * 2;

        it = find(byly.begin(), byly.end(), x);
        if (it != byly.end()) {
            return byly[(it - byly.begin()) +
                        ((n - i - 1) % (byly.size() - (it - byly.begin())))];
        }
        ++i;
    }
    return x;
}

int main() {
    cin >> n >> x;
    cout << podaj_n_ciagu() << "\n";
}