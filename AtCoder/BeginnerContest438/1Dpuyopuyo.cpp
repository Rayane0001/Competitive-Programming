#include <iostream>
#include <algorithm>
#include <vector>
#include<cmath>
#include <stack>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    vector<int> st;
    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        st.push_back(x);
        while (st.size() >= 4 &&
            st.back() == st[st.size()-2] &&
            st.back() == st[st.size()-3] &&
            st.back() == st[st.size()-4]) {
                st.pop_back();
                st.pop_back();
                st.pop_back();
                st.pop_back();
        }
    }

    cout << st.size() << endl;
}