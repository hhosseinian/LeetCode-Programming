from typing import List
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        n = len(nums)
        Output =[]

        def binary_search_first(nums: List[int], target: int) -> int:
            left,right = 0,n-1
            result = -1
            while left<=right:
                mid =(left+right)//2
                if nums[mid] == target:
                    result = mid
                    right = mid-1
                elif nums[mid] < target:
                    left = mid+1
                else:
                    right = mid-1
            return result
        def binary_search_second(nums: List[int], target: int) -> int:
            left,right = 0,n-1
            result = -1
            while left<=right:
                mid =(left+right)//2
                if nums[mid] == target:
                    result = mid
                    left = mid+1
                elif nums[mid] < target:
                    left = mid+1
                else:
                    right = mid-1
            return result

        first_index = binary_search_first(nums, target)
        last_index = binary_search_second(nums, target)
        if first_index == -1:  # Target not found
            return []
        for i in range(first_index,last_index+1):
            Output.append(i)
        return Output
