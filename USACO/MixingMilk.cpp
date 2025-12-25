#include <array>
#include <iostream>
#include <vector>

using namespace std;

int main()
{
    freopen("mixmilk.in", "r", stdin);
    freopen("mixmilk.out", "w", stdout);
    
    vector<array<int, 2>> v(3);
    for (int i = 0; i < 3; ++i) {
        cin >> v[i][0] >> v[i][1];
    }
    // [0] = max capacity
    // [1] = what's inside the bucket
    
    for (int pour = 0; pour < 100; ++pour) {
        int from = pour % 3;
        int to = (pour + 1) % 3;
        
        int can_pour = v[to][0] - v[to][1];
        if (can_pour <= v[from][1]) {
            v[to][1] = v[to][0];
            v[from][1] -= can_pour;
        } else {
            v[to][1] += v[from][1];
            v[from][1] = 0;
        }
    }
    
    cout << v[0][1] << "\n";
    cout << v[1][1] << "\n";
    cout << v[2][1] << "\n";
    
    return 0;
}