class Solution {
public:
    string reverseOnlyLetters(string s) {
        int l = 0;
        int r = s.size() - 1;

        while (l <= r) {
            // while (s[l] < 'A' && s[l] > 'Z' || s[l] < 'a' && s[l] > 'z') {
            //     l++;
            // }

            // while (s[r] < 'A' && s[r] > 'Z' || s[r] < 'a' && s[r] > 'z') {
            //     r--;
            // }

            while (!isalpha(s[l]) && l < r) l++;
            while (!isalpha(s[r]) && l < r) r--;

            swap(s[l], s[r]);
            l++;
            r--;
        }

        return s;
    }
};