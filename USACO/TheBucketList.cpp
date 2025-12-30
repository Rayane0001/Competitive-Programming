#include <algorithm>
#include <iostream>
#include <vector>
#include <array>

using namespace std;

int main() {
    freopen("blist.in", "r", stdin);
    freopen("blist.out", "w", stdout);

    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    vector<array<int, 3>> v(n);
    for (int i =0; i<n; i++) {
        cin >> v[i][0] >> v[i][1] >> v[i][2]; // begin | end | buckets required
    }

    // strategy : iterate all elements, and store the current number of bucket and max_bucket if we find it
    int max_bucket =0;

    for (int i =0; i<n; i++) {
        int bucket = 0;
        int time = v[i][0];
        for (int j=0; j<n; j++) {
            if (v[j][0] <= time && time <= v[j][1]) {
                bucket += v[j][2];
                if (bucket >= max_bucket) {
                    max_bucket = bucket;
                }
            }
        }
    }

    cout << max_bucket;
}