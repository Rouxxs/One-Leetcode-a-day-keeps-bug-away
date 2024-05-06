class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        int count[26] = {0};
        for(int i = 0; i < tasks.size(); i++) {
            count[tasks[i] - 'A']++;
            
        }
        int n_ = sizeof(count) / sizeof(count[0]);

        sort(count, count + n_, greater<int>());

        int idle = n * (count[0] - 1);
        int total = count[0] + idle;

        for(int i = 1; i < 26 && count[i] != 0; i++) {
            if (idle >= count[i]) {
                if (count[i] == count[0]) {
                    idle -= count[i] - 1;
                    total++;
                } else {
                    idle -= count[i];
                }
            } else {
                return tasks.size();
            }
        }

        return total;
    }
};