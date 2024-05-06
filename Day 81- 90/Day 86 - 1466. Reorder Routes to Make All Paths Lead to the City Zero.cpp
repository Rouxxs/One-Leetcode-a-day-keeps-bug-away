class Solution {
public:
// Every node has only one parent in the tree -> pass the prev node instead of visited vector
    int dfs(vector<vector<int>> &alist, int prev, int curr) {
        int change = 0;
        for (auto x : alist[curr]) {
            change += (abs(x) == prev ? 0 : dfs(alist, curr, abs(x)) + (x > 0));
        }
        return change;
    }
    int minReorder(int n, vector<vector<int>>& connections) {
        vector<vector<int>> alist(n);
        for (auto &x : connections) {
            alist[x[0]].push_back(x[1]);
            alist[x[1]].push_back(-x[0]);
        }
        return dfs(alist, 0, 0);
    }
};