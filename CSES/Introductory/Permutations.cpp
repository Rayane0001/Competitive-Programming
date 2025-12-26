#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    if (n>1 && n <4) {
        cout << "NO SOLUTION";
        return 0;
    }

    vector<int> v(n);
    for (int i =0; i<n; i++) {
        v[i] = i+1;
    }

    for (int i = 1; i<n; i+=2) {
        cout << v[i] << " ";
    }

    for (int i =0; i<n; i+=2) {
        cout << v[i] << " ";
    }

    return 0;
}