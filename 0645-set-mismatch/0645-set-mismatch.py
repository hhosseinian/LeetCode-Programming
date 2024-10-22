class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        hash_map = {}
        result = []
        for digit in nums:
            if digit in hash_map:
                result.append(digit)
                hash_map[digit] +=1
            else:
                hash_map[digit] = 1
        for i in range(1,len(nums)+1):
            if i not in hash_map:
                result.append(i)
        return result
