class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        int result = 0;
        vector<int> localvec = flowerbed;
        int l = flowerbed.size();
        if (l == 1) {
            if (localvec[0] == 0)
                return n <= 1;
            return n == 0;
        }
        if (localvec[0] == 0 && localvec[1] == 0) {
            result++;
            localvec[0] = 1;
        }cout <<localvec[0];
        if (localvec[l - 1] == 0 && localvec[l - 2] == 0) {
            result++;
            localvec[l - 1] = 1;
        }
        for (int i = 1; i < l - 1; i++) {
            if (localvec[i - 1] == 0 && localvec[i] == 0 &&
                localvec[i + 1] == 0) {
                result++;
                localvec[i] = 1;
            }
            cout <<localvec[i];
            //if (result == n)
             //   return true;
        }cout <<localvec[l - 1];
        return result >= n;
    }
};