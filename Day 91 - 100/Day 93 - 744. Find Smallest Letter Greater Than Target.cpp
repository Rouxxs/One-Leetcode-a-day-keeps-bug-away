class Solution {
public:
    char nextGreatestLetter(vector<char>& letters, char target) {
        if (letters.back() <= target) return letters.front();
        int l = 0, r = letters.size() - 1;

        while (l < r) {
            int mid = (r + l) / 2;
            if (target < letters[mid]) r = mid;
            else l = mid + 1;
        }

        return letters[l];
    }
};