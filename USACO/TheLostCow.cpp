#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    freopen("lostcow.in", "r", stdin);
    freopen("lostcow.out", "w", stdout);

    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int x, y;
    cin >> x >> y;

    int distance = 0;
    int i = 1;

    while (true) {
        int target = x + i;

        if ((i > 0 && y >= x && y <= target) ||
            (i < 0 && y <= x && y >= target)) {
            distance += abs(y - x);
            break;
            }

        distance += abs(i);
        distance += abs(i);

        i *= -2;
    }

    cout << distance << endl;

    return 0;
}