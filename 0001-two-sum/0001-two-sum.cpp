class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> hash; //hash: number->index
        for(int i=0; i<nums.size(); ++i){
            int complement = target-nums[i];
            if (hash.count(complement)){
                return {hash[complement],i};
            }else{
                hash[nums[i]]=i;
            }
        }
        return {};
    }
};