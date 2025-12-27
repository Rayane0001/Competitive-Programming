#include <iostream>
#include <algorithm>
#include <vector>
#include<cmath>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int d,f;
    cin >> d >> f;

    while (f <= d) {
        f += 7;
    }

    cout << f-d;
}