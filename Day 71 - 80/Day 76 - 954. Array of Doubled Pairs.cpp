class Solution {
public:
    bool canReorderDoubled(vector<int>& arr) {
        unordered_map<int, int> count;
        for (auto a : arr) {
            count[a]++;
        }
        vector<int> keys;
        for (auto c : count) {
            keys.push_back(c.first);
        }
        sort(keys.begin(), keys.end(), [](int i, int j) {return abs(i) < abs(j);});
        for (auto x : keys) {
            if (count[x * 2] < count[x]) {
                return false;
            }
            count[x * 2] -= count[x];
        }
        return true;
    }
};