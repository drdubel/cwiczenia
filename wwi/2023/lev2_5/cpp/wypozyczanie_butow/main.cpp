#include <iostream>
#include <algorithm>

using namespace std;

const int MAXN = 5e5 + 7;
int buty[MAXN], pieniadze[MAXN], n, m, a, i, mi, ni, kupione_buty;
    
int main() {
    cin >> n >> m >> a;
    for (; i < n; ++i) {
        cin >> pieniadze[i];
    }
    for (i = 0; i < m; ++i) {
        cin >> buty[i];
    }
    sort(buty, buty + m);
    sort(pieniadze, pieniadze + n);
    i = 0;
    while (mi < m && ni < n) {
	    if (pieniadze[ni] < buty[mi]) {
            if (a < buty[mi] - pieniadze[ni]) {
                ni += 1;
                continue;
            }
            a -= buty[mi] - pieniadze[ni];
        }
        ++kupione_buty;
        ++mi;
        ++ni;
    }
    cout << kupione_buty << "\n";
}
