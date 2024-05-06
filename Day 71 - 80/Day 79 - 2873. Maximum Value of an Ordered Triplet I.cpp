class Solution {
public:
    long long maximumTripletValue(vector<int>& nums) {
        long long ans = 0;
        int maxij = 0, maxi = 0;
        for (int k = 0; k <= nums.size() - 1; k++) {
            ans = max(ans, 1LL * maxij * nums[k]);
            maxij = max(maxij, maxi - nums[k]);
            maxi = max(maxi, nums[k]);
        }
        return ans;
    }
};