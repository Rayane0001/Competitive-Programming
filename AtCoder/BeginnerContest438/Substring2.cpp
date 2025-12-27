#include <iostream>
#include <algorithm>
#include <vector>
#include<cmath>
#include <limits.h>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m; // lengths
    string s, t; // s is length n et t is length m
    // s & t are from 0 to 9
    cin >> n >> m >> s >> t;

    int cost;
    int min_cost = INT_MAX;
    int range = n-m;
    // for the circular distance I think that this would
    // be a correct formula : (S[i+j] - T[j] + 10) % 10
    //
    for (int i =0; i<=range; i++) {
        cost = 0;
        for (int j =0; j<m; j++) { // for each number inside t
            cost += (s[i+j] - t[j] + 10) % 10;
        }
        if (cost < min_cost) {
            min_cost = cost;
        }
    }
    cout << min_cost;
}