class Solution {
public:
    int maximumScore(vector<int>& scores, vector<vector<int>>& edges) {
        set<pair<int, int>> graph[scores.size()];

        for (auto edge : edges) {
            graph[edge[0]].insert({scores[edge[1]], edge[1]});
            graph[edge[1]].insert({scores[edge[0]], edge[0]});

            if (graph[edge[0]].size() > 3) graph[edge[0]].erase(graph[edge[0]].begin());
            if (graph[edge[1]].size() > 3) graph[edge[1]].erase(graph[edge[1]].begin());
        }

        int res = -1;

        for (auto edge : edges) {
            for (auto i : graph[edge[0]]) {
                for (auto j : graph[edge[1]]) {
                    if (i.second != j.second && i.second != edge[1] && j.second != edge[0]) {
                        res = max(res, scores[edge[0]] + scores[edge[1]] + i.first + j.first);
                    }
                }
            }
        }
        return res;
    }
};