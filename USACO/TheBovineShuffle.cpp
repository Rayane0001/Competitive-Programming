#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
    freopen("shuffle.in", "r", stdin);
    freopen("shuffle.out", "w", stdout);

    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int nb_cows;
    cin >> nb_cows;
    vector<int> shuffle(nb_cows);
    vector<int> random(nb_cows);
    for (int i = 0; i < nb_cows; i++) {
        cin >> shuffle[i];
        shuffle[i]--;
    }
    for (int i = 0; i < nb_cows; i++) {
        cin >> random[i];
    }
    vector<int> current = random;
    for (int i = 0; i < 3; i++) {
        vector<int> temp(nb_cows);
        for (int j = 0; j < nb_cows; j++) {
            temp[j] = current[shuffle[j]];
        }
        current = temp;
    }
    for (int i = 0; i < nb_cows; i++) {
        cout << current[i] << endl;
    }
    return 0;
}