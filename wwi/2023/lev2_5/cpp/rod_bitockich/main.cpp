#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int MAXN = 3e5 + 7;
int przodkowie[MAXN], n, m, d, a, b, i, j;
vector<int> dzieci[MAXN];

int lca(int a, int b) {
    vector<int> byly;
    int c = min(a, b);
    b = max(a, b);
    a = c;
    while (a != 0) {
        byly.push_back(a);
        a = przodkowie[a];
    }
    while (b != 0) {
        if (count(byly.begin(), byly.end(), b) > 0) {
            return b;
        }
        b = przodkowie[b];
    }
    return 0;
}

pair<int, int> dlugosc_rozmowy(int a, int b) {
    int wspol_przod = lca(a, b);
    int min_dlug = 1e9, max_dlug = 0;
    if (wspol_przod == a || wspol_przod == b) {
        wspol_przod = przodkowie[wspol_przod];
    }
    while (wspol_przod != 0) {
        max_dlug = max(max_dlug, (int)dzieci[wspol_przod].size() + 1);
        min_dlug = min(min_dlug, (int)dzieci[wspol_przod].size() + 1);
        wspol_przod = przodkowie[wspol_przod];
    }
    max_dlug = max(max_dlug, (int)dzieci[wspol_przod].size() + 1);
    min_dlug = min(min_dlug, (int)dzieci[wspol_przod].size() + 1);
    return {min_dlug, max_dlug};
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cin >> n;
    for (i = 1; i < n; ++i) {
        cin >> d;
        dzieci[d].push_back(i);
        przodkowie[i] = d;
    }
    cin >> m;
    for (i = 0; i < m; ++i) {
        cin >> a >> b;
        pair<int, int> dlugosci = dlugosc_rozmowy(a, b);
        cout << dlugosci.first << " " << dlugosci.second << "\n";
    }
}