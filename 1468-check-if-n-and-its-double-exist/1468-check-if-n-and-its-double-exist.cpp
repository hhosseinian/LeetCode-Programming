class Solution {
public:
    bool checkIfExist(vector<int>& arr) {
        unordered_map<int,bool> seen;
        for(int i=0;i<arr.size();++i){
            if (seen[2*arr[i]] || (arr[i]%2 ==0 && seen[arr[i]/2])){
                return true;
            }
            else{
                seen[arr[i]]=true;
            }
        }
        return false;
    }
};