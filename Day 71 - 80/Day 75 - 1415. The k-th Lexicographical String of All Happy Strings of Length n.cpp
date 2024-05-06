class Solution {
public:
    void gen(vector<string> &ans, string &s, int n, int k){
        if (ans.size() == k) return;
        if (s.length() == n) {
            ans.push_back(s);
            return;
        }
        int i = s.length() - 1;
        vector<char> set = {'a', 'b', 'c'};
        for (int j = 0; j < 3; j++) {
            if (s.size() == 0 || s[s.size() - 1] != set[j]) {
                s += set[j];
                gen(ans, s, n, k);
                s.pop_back();
            }
            // cout << s << endl;
        }
    }
    string getHappyString(int n, int k) {
        vector<string> ans; 
        string s = "";
        gen(ans, s, n, k);
        for (auto x: ans) {
            cout << x << endl;
        }
        if (ans.size() == k) {
            return ans.back();
        }
        return "";
    }
};