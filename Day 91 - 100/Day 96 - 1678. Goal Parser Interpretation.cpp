class Solution {
public:
    string interpret(string command) {
        stack<char> s;
        string ans = "";
        for (auto c : command) {
            if (c == 'G') {
                ans += c;
                continue;
            }
            if (s.empty()) {
                s.push(c);
                continue;
            }
            if (s.top() == '(') {
                if (c == ')'){
                    ans += 'o';
                } else {
                    ans += "al";
                }
                s.pop();
            } else {
                s.push(c);
            }
        }
        return ans;
    }
};