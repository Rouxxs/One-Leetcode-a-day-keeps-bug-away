class Solution {
public:
    vector<int> findPeaks(vector<int>& mountain) {
        vector<int> ans;
        int n = mountain.size();
        for (int i = 1; i < n;){
            if (i == n - 1) break;
            if (mountain[i - 1] < mountain[i] && mountain[i + 1] < mountain[i]) {
                ans.push_back(i);
                i += 2;
            } else {
                i++;
            }
        }
        return ans;
    }
};