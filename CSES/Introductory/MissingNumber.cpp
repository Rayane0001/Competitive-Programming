#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    vector<int> v(n-1);
    for (int i =0; i<n-1; i++) {
        cin >> v[i];
    }

    int missing;
    sort(v.begin(), v.end());
    for (int i = 0; i<n-1;i++) {
        if (v[i] != i+1) {
            missing = i+1;
            cout << missing;
            return 0;
        }
    }

    cout << n;

    return 0;
}
