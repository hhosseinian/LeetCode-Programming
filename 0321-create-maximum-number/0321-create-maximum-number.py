class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def pick(nums, count):
            stack = []
            drop =len(nums)-count
            for num in nums:
                while drop>0 and stack and stack[-1]<num:
                    stack.pop()
                    drop-=1
                stack.append(num)
            return stack[:count]
        def merge(nums1,nums2):
            return [max(nums1,nums2).pop(0) for _ in range(len(nums1)+len(nums2))]
        max_result =[]
        n1,n2 = len(nums1),len(nums2)
        for i in range(max(0,k-n2), min(n1,k)+1):
            j = k-i
            if j>n2 or j<0:
                continue
            max1 = pick(nums1,i)
            max2 = pick(nums2,j)
            combined=merge(max1,max2)
            max_result = max(max_result,combined)
        return max_result
    