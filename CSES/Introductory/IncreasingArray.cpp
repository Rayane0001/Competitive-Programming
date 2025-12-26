#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    cin >> n;

    vector<long long> v(n);
    for (long long i =0; i<n; i++) {
        cin >> v[i];
    }

    long long added = 0;

    for (long long i =1; i<n; i++) {
        if (v[i] < v[i-1]) {
            long long add = v[i-1] - v[i];
            added += add;
            v[i] += add;
        }
    }

    cout << added;
}