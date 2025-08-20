class Solution {
public:
#include <unordered_map>
    int maxOperations(vector<int>& nums, int k) {
        int countx;
        int x;
        int k_x;
        int countk_x;
        int Out = 0;
        std::unordered_map<int, int> frequencyMap;
        for (int num : nums) {
            frequencyMap[num]++;
        }
        for (auto s:frequencyMap) {
            x = s.first;
            k_x = k-x;
            countx = frequencyMap[x];
            if (x==k_x){Out+=countx;}
            else{
                if (frequencyMap.find(k_x) != frequencyMap.end()) {
                    countk_x = frequencyMap[k_x];
                    Out+=min(countx,countk_x);
                }
            }
            }
        return Out/2;
    }
};