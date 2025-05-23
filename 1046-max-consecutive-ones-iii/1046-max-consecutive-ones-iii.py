class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n=len(nums)
        if n==1:
            return 1 if(k==1 or nums[0]==1) else 0
        left,right = 0,1
        max_ones = 0 
        flipped_zeros = 0
        for right in range(n):
            if nums[right]==0:
                flipped_zeros+=1
            while flipped_zeros>k:
                if nums[left]==0:
                    flipped_zeros-=1
                left+=1
            max_ones =max(max_ones,right-left+1)
        return max_ones
                


                