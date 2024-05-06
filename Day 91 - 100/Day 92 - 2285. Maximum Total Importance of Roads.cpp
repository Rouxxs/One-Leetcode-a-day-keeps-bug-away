class Solution {
public:
    long long maximumImportance(int n, vector<vector<int>>& roads) {
        long long ans = 0;
        vector<int> cityRoads(n, 0);

        for (auto r : roads) {
            cityRoads[r[0]]++;
            cityRoads[r[1]]++;
        }

        sort(cityRoads.begin(), cityRoads.end());

        for (int i = 0; i < n; i++) {
            ans += (long long) cityRoads[i] * (i + 1);
        }

        return ans;
    }
};