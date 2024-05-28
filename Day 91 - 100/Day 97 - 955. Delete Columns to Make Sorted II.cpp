class Solution {
public:
    int minDeletionSize(vector<string>& strs) {
        int n = strs.size();
        int m = strs[0].size();
        int ans = 0;
        vector<bool> sorted(n, true);
        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < m; j++) {
                if (!sorted[j] || strs[i][j] == strs[i+1][j]) continue;
                if (strs[i][j] > strs[i+1][j]) {
                    sorted[j] = false;
                    i = -1;
                    ans++;
                }
                break;
            }
        }
        return ans;
    }
};