#include <cmath>
#include <iostream>

using namespace std;

int n;
long long x, y, m, value, i;

int main() {
    scanf("%d", &n);
    for (; i < n; ++i) {
        scanf("%lld%lld", &y, &x);
        m = max(x, y);
        value = m * (m - 1) + 1 + (y - x) * (m % 2 * -2 + 1);
        printf("%lld\n", value);
    }
}