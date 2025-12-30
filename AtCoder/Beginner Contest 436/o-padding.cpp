#include <iostream>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    string s;
    cin >> s;

    int to_add = n - s.length();

    for (int i= 0; i<to_add; i++) {
        s = "o" + s;
    }
    cout << s;
}