#include <iostream>
#include <algorithm>
#include <array>
#include <vector>

using namespace std;

int main() {
    freopen("speeding.in", "r", stdin);
    freopen("speeding.out", "w", stdout);

    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n,m;

    cin >> n >> m;

    vector<array<int, 2>> road(n); // length & speed limit
    vector<array<int, 2>> journey(m); // length & speed driving

    for (int i = 0; i<n; i++) {
        cin >> road[i][0] >> road[i][1];
    }

    for (int i = 0; i<m; i++) {
        cin >> journey[i][0] >> journey[i][1];
    }

    array<int, 100> limits;
    array<int, 100> speed;

    int position = 0;
    for (int i =0; i<n; i++) {
        for (int j =0; j< road[i][0]; j++) {
            limits[position] = road[i][1];
            position ++;
        }
    }
    position = 0;
    for (int i =0; i<m; i++) {
        for (int j =0; j< journey[i][0]; j++) {
            speed[position] = journey[i][1];
            position ++;
        }
    }

    int over_max = 0;

    for (int i = 0; i <100; i++) {
        if (speed[i] > limits[i]) {
            int over = speed[i] - limits[i];
            if (over > over_max) {
                over_max = over;
            }
        }
    }

    cout << over_max;
}