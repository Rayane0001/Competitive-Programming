#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    cin >> n;

    vector<long long> v(n-1);
    for (long long i =0; i<n-1; i++) {
        cin >> v[i];
    }

    long long correct_sum = n * (n+1) / 2;
    long long current_sum = 0;
    for (long long i =0; i<n-1; i++) {
        current_sum += v[i];
    }

    long long difference = correct_sum - current_sum;

    cout << difference;

    return 0;
}
