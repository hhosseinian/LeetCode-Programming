class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target>letters[-1] or target<letters[0]:
            return letters[0]
        n = len(letters)
        left,right = 0,n
        while left<right:
            mid =(left+right)//2
            if letters[mid]<=target:
                left = mid+1
            else:
                right = mid
        return letters[left%n]