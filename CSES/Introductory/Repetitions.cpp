#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    cin >> s;

    int max_length = 0;
    int current_length = 0;
    for (int i = 0; i<s.length(); ++i) {

        if (i > 0 && s[i] != s[i-1]) {
            current_length = 1;
        } else {
            current_length += 1;
        }
        if (current_length > max_length) {
            max_length = current_length;
        }
    }

    cout << max_length;
}