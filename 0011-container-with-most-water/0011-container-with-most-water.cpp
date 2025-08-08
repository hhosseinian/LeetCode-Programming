class Solution {
public:
    int maxArea(vector<int>& height) {
        int Out = 0;
        int n = height.size();
        int j = n;
        for (int i=0;i<n;i++){
            j = n;
            while (Out<(j-i)*height[i]){
                j--;
                Out = max(Out,min(height[i],height[j])*(j-i));
            }    
        }
        return Out;
    }
};