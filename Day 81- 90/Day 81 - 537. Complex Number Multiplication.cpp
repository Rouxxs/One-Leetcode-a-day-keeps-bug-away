class Solution {
public:
    int real(string s) {
        int i = 0;
        string r = "";
        while (s[i] != '+') {
            r += s[i];
            i++;
        }
        return stoi(r);
    }

    int imaginary(string s) {
        int i = 0;
        while (s[i++] != '+') {} 
        string im = "";
        while (s[i] != 'i') {
            im += s[i];
            i++;
        }
        return stoi(im);
    }
    string complexNumberMultiply(string num1, string num2) {
        string ans = "";
        int a1 = real(num1);
        int a2 = real(num2);
        int b1 = imaginary(num1);
        int b2 = imaginary(num2);

        ans += to_string(a1 * a2 - b1 * b2) + '+' + to_string(a1 * b2 + a2 * b1) + 'i';
        return ans;
    }
};