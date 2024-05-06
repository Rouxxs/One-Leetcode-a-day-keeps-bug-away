class Solution {
public:
    int minBitFlips(int start, int goal) {
        int ans = 0;
        while (start > 0 || goal > 0) {
            int b1 = start&1;
            int b2 = goal&1;

            if (b1 != b2) {
                ans++;
            }

            start = start >> 1;
            goal = goal >> 1;
            // cout << b1 << ' ' << b2 << endl;
        }
        return ans;
    }
};