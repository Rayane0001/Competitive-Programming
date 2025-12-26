#include <iostream>
#include <algorithm>
#include <vector>
#include <set>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    long long sum = n*(n+1) / 2;

    if (sum % 2 != 0) { // if the sum cannot be divided by 2
        cout << "NO";
        return 0;
    }

    vector<int> set1;
    vector<int> set2;

    long long sum1 =0;
    long long sum2 =0;

    for (int i = n; i >0; i--) {
        if (sum1 <= sum2) {
            set1.push_back(i);
            sum1 += i;
        } else {
            set2.push_back(i);
            sum2 +=i;
        }
    }

    cout << "YES" << endl;
    cout << set1.size() << endl;
    for (int i : set1) {
        cout << i << " ";
    }
    cout << "\n" << set2.size() << endl;
    for (int i : set2) {
        cout << i << " ";
    }
}