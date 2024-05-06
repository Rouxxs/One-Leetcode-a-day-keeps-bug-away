class Solution {
public:
    string minimizeStringValue(string s) {
        vector<int> aphab(26);
        string marks = "";
        int count = 0;
        for (int i = 0; i < s.size(); i++) {
            if (s[i] == '?') {
                count++;
            }
            else {
                aphab[s[i] - 'a']++;
            }
        }

        for (int i = 0; i < count; i++) {
            int tmp = s.size();
            int j;
            for(int k = 0; k < 26; k++) {
                if (aphab[k] < tmp) {
                    tmp = aphab[k];
                    j = k;
                }
            }
            marks += ('a' + j);
            aphab[j]++;
        }

        sort(marks.begin(), marks.end());
        string ans = "";
        int idx = 0;
        for (int i = 0; i < s.size(); i++) {
            if (s[i] == '?') {
                s[i] = marks[idx++];
            }
        }
        return s;
    }
};