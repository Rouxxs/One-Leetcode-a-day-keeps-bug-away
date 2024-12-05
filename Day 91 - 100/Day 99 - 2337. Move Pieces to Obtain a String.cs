public class Solution {
    public bool CanChange(string start, string target) {
        int j = 0;
        int i = 0;
        int n = start.Length;
        while (j < n || i < n) {
            while (i < n && start[i] == '_') {
                i++;
            }
            while (j < n && target[j] == '_') {
                j++;
            }

            if (i == n || j == n || start[i] != target[j] || (start[i] == 'L' && i < j) || (start[i] == 'R' && i > j)) {
                break;
            }
            j++;
            i++;
        }
        
        return i == n && j == n;
    }
}