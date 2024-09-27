class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        distinct1 = []
        distinct2 = []
        for i in nums1:
            if i not in nums2:
                if i not in distinct1:
                    distinct1.append(i)
        for i in nums2:
            if i not in nums1:
                if i not in distinct2:
                    distinct2.append(i)
        return [distinct1,distinct2]