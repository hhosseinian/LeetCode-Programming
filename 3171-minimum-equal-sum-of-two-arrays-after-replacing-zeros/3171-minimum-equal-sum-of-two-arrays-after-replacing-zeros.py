class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum1, count1 = sum(x for x in nums1), nums1.count(0)
        sum2, count2 = sum(x for x in nums2), nums2.count(0)
        if ((sum1 < sum2 + count2) and count1 ==0 ) or ((sum2 < sum1 + count1) and count2 ==0 ):
            return -1
        return max(sum1 + count1, sum2 + count2)


        