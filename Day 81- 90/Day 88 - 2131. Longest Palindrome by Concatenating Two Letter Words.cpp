class Solution {
public:
    int longestPalindrome(vector<string>& words) {
        int ans = 0;
        unordered_map<string, int> mp;
        for (auto w : words) {
            string r = w;
            reverse(r.begin(), r.end());
            if (mp[r] > 0) {
                ans += 4;
                mp[r]--;
            } else {
                mp[w]++;
            }
        }

        for (auto i : mp) {
            if (i.first[0] == i.first[1] && i.second > 0) {
                return ans + 2;
            }
        }
        return ans;
    }
};