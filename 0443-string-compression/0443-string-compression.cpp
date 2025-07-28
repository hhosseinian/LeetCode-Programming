class Solution {
public:
    int compress(vector<char>& chars) {
        int n = chars.size();
        if (n == 1)
            return 1;
        string s = "";
        int ptr = 0;
        int i = 0;
        while (i < n) {
            ptr = i;
            s += chars[ptr];
            while (i<n && ptr<n && chars[i] == chars[ptr]) {
                i++;
            }
            if (i - ptr > 1)
                s += to_string(i - ptr);
        }
        for (int i = 0; i < s.size(); i++) {
            chars[i] = s[i];
        }
        return s.size();
    }

};