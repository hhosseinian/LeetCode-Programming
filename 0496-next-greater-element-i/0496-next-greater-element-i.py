class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1,n2 = len(nums1),len(nums2)
        next_greater = {}
        stack =[]
        for j in range(n2):
            while stack and nums2[j]>stack[-1]:
                next_greater[stack[-1]]=nums2[j]
                stack.pop()
            stack.append(nums2[j])
        return [next_greater.get(num,-1) for num in nums1]