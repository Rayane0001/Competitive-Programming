#include <iostream>
#include <vector>
#include <algorithm>

using namespace  std;

int main(){

    freopen("cowsignal.in", "r", stdin);
    freopen("cowsignal.out", "w", stdout);

    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int m, n, k;
    cin >> m >> n >> k;

    vector<string> v(m);
    for (int i =0; i<m; i++) {
        cin >> v[i];
    }

    for (int i =0; i<m; i++) {
        string line = "";
        for (int j = 0; j<n; j++) {
            string repeat(k, v[i][j]);
            line += repeat;
        }
        for (int rep = 0; rep <k; ++rep) {
            cout << line << endl;
        }
    }
}