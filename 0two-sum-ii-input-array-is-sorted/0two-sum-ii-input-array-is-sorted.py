class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        for index1 in range(len(numbers)-1):
            index2 = index1+1
            if numbers[-1]<target-numbers[index1]:
                continue
            while numbers[index2]<target-numbers[index1]:
                index2+=1
            if numbers[index2]==target-numbers[index1]:
                return [index1+1,index2+1]
        return [-1,-1]
            
        