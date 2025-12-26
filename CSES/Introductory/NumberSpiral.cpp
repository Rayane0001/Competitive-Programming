#include <iostream>
#include <vector>
#include <algorithm>
#include <array>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;

    vector<array<int, 2>> v(t); // row | column
    for (int i =0; i<t; i++) {
        cin >> v[i][0] >> v[i][1];
    }

    

}