class Solution {
public:
    bool checkIfExist(vector<int>& arr) {
        unordered_map<int,bool> seen;
        for(int i=0;i<arr.size();++i){
            if (seen.count(2*arr[i]) || (arr[i]%2 ==0 && seen.count(arr[i]/2))){
                return true;
            }
            else{
                seen[arr[i]]=true;
            }
        }
        return false;
    }
};