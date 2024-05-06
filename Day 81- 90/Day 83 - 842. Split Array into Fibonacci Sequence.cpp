class Solution {
public:
    vector<int> splitIntoFibonacci(string num) {
        vector<int> ans;
        backtracking(num, 0, ans);
        return ans;
    }
    bool backtracking(string s, int idx, vector<int>& ans) {
        int n = s.size();
        cout << "idx " << idx << endl;
        if(idx >= n && ans.size()>=3){
            return true;
        }

        long num = 0;
        for (int i = idx; i < n; i++) {
            if (s[idx] == '0' && i > idx) break;
            num = 10 * num + (s[i] - '0');

            if (num > INT_MAX) return false;
            //if (aSize >= 2 && ans[aSize - 1] + ans[aSize - 2] < num) return false;
            
            if(ans.size()<=1 || num==(long)ans[ans.size()-1]+(long)ans[ans.size()-2]) {
                cout<<"push " << num << endl;
                ans.push_back(num);
                if (backtracking(s, i + 1, ans)) {
                    cout << "test" << endl;
                    return true;
                }
                ans.pop_back();
                cout << "pop " << num << endl;
            }
        }
        return false;
    }
};