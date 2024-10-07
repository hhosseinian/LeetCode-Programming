class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:  # Handle 0 and 1 as special cases
            return True
        left,right = 0,num
        while left<=right:
            mid = (left+right)//2
            mid_sq =mid*mid
            if mid_sq == num:
                return True
            elif mid_sq < num:
                left = mid+1
            else:
                right = mid-1
        return False