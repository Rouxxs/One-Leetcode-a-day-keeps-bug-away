class Solution {
public:
    int rotatedDigits(int n) {
        int count = 0;
        
        int valid[] = {1, 1, 2, 0, 0, 2, 2, 0, 1, 2};
        for (int i = 1; i <= n; i++)
        {
            int check = 1;
            int tmp = i;
            while (tmp) {
                check *= valid[tmp%10];
                tmp /= 10;
            }
            
            if (check >= 2) count++;
         }
        return count;
        
    }
};