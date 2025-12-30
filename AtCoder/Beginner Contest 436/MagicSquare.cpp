#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    vector<vector<int>> grid(n, vector<int>(n, 0));
    grid[0][(n-1)/2] = 1;
    int r = 0;
    int c = (n-1)/2;
    int last_written = 1;
    for (int i=0; i<(n*n)-1; i++) {
        if (grid[((r-1)+n)%n][(c+1)%n] == 0) {
            r = ((r-1)+n)%n;
            c = (c+1)%n;
            grid[r][c] = last_written +1;
        } else {
            r = r+1%n;
            grid[r][c] = last_written+1;
        }
        last_written += 1;
    }

    for (int i =0; i<n; i++) {
        for (int j = 0; j<n; j++) {
            cout << grid[i][j] << " ";
        }
        cout << endl;
    }
}