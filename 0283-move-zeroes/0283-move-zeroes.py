class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zc=0
        t = 0
        N=len(nums)
        for i in range(N-zc):
            if nums[i+t] == 0:
                del nums[i+t]
                nums.append(0)
                zc += 1
                t -= 1

        return nums