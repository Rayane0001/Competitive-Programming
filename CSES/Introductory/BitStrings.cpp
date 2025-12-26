#include <iostream>
#include <algorithm>
#include <vector>
#include<cmath>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    long long res = 1;
    long long mod = 1000000007;
    for (int i =0; i<n; i++) {
        res *=2;
        res = res % mod;
    }
    cout << res;
    return 0;
}