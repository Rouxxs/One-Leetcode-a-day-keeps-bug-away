class Solution {
public:
    bool escapeGhosts(vector<vector<int>>& ghosts, vector<int>& target) {
        int distance = abs(target[0]) + abs(target[1]);
        for (auto g: ghosts) {
            if (distance >= abs(target[0] - g[0]) + abs(target[1] - g[1])) return false;
        }
        return true;
    }
};