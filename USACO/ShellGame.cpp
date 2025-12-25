#include <algorithm>
#include <array>
#include <iostream>
#include <vector>

using namespace std;

using namespace std;

int main()
{
    freopen("shell.in", "r", stdin);
    freopen("shell.out", "w", stdout);
    
    int n;
    cin >> n;
    
    vector<array<int, 3>> operations(n);
    for (int i = 0; i < n; i++) {
        cin >> operations[i][0] >> operations[i][1] >> operations[i][2];
        operations[i][0] = operations[i][0] - 1;
        operations[i][1] = operations[i][1] - 1;
        operations[i][2] = operations[i][2] - 1;
    }
    
    int max_score = 0;
    
    for (int start = 0; start < 3; start++) {
        vector<int> shell_at_pos(3);
        for (int i = 0; i < 3; i++) {
            shell_at_pos[i] = i;
        }
        
        int score = 0;
        int pebble_pos = start;
        
        for (int i = 0; i < n; i++) {
            int a = operations[i][0];
            int b = operations[i][1];
            int g = operations[i][2];
            
            swap(shell_at_pos[a], shell_at_pos[b]);
            
            if (pebble_pos == a) {
                pebble_pos = b;
            } else if (pebble_pos == b) {
                pebble_pos = a;
            }
            
            if (pebble_pos == g) {
                score++;
            }
        }
        
        max_score = max(max_score, score);
    }
    
    cout << max_score << "\n";
    
    return 0;
}