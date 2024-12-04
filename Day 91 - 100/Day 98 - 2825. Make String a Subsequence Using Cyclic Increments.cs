public class Solution {
    private bool Check(char a, char b) {
        a++;
        if (a > 'z') a = 'a';
        return a == b;
    }
    public bool CanMakeSubsequence(string str1, string str2) {
        int j = 0;
        for (int i = 0; i < str1.Length; i++) 
        {
            if (j < str2.Length && (str1[i] == str2[j] || Check(str1[i], str2[j]))) {
                j++;
            }
        }

        return j == str2.Length;
    }
}