class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        n = len(s)
        s_list =list(s)
        partitions = n//(2*k)
        for i in range(partitions):
            left,right = i*2*k,i*(2*k)+k-1
            while left<right:
                s_list[left],s_list[right] = s_list[right],s_list[left]
                left+=1
                right-=1
        if  n%(2*k)<k:
            left,right = partitions*2*k,n-1
        elif k<=n%(2*k)<2*k:
            left,right = partitions*2*k,partitions*2*k+k-1
        while left<right:
            s_list[left],s_list[right] = s_list[right],s_list[left]
            left+=1
            right-=1
        return ''.join(s_list)

