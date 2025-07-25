class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        int n1 = word1.size();
        int n2 = word2.size();
        int n_min =min(n1,n2);
        string out ="";
        int ptr =0;
        while(ptr<n_min){
            out+=word1[ptr];
            out+=word2[ptr];
            ptr++;
        }
        out+=word1.substr(ptr,n1-ptr);
        out+=word2.substr(ptr,n2-ptr);
        return out;
        
    }
};