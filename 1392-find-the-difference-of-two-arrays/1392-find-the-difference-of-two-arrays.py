class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # Convert both lists to sets for distinct elements
        set1 = set(nums1)
        set2 = set(nums2)
    
        # Find distinct elements in nums1 not in nums2 and vice versa
        distinct_in_nums1 = list(set1 - set2)
        distinct_in_nums2 = list(set2 - set1)
    
        return [distinct_in_nums1, distinct_in_nums2]