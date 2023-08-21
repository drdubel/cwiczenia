#include <iostream>

using namespace std;

const int MAXN = 1e6 + 7;
int p[MAXN];
string word;

void kmp() {
    p[0] = -1;
    int l = 0;
    for (int i = 2; i < word.size(); ++i) {
        while (l > 0 && word[l + 1] != word[i]) l = p[l];
        if (word[i] == word[l + 1]) ++l;
        p[i] = l;
    }
}

int main() {
    cin >> word;
    word = "$" + word;
    kmp();
    for (int i = 1; i < word.size(); ++i) {
        p[i] > 0 ? cout << 1 : cout << 0;
    }
    cout << "\n";
}