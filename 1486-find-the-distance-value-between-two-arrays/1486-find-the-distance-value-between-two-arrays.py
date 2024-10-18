class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        def binary_search(arr,target):
            n = len(arr)
            left,right = 0,n-1
            if target <= arr[left]:
                return arr[left]
            if target >= arr[right]:
                return arr[right]
            while left<=right:
                mid = (left+right)//2
                if arr[mid]==target:
                    return arr[mid]
                elif arr[mid]<target:
                    left = mid+1
                else: 
                    right = mid-1
            closest_value = None
            if left < len(arr):
                closest_value =arr[left]
            if right >= 0:
                if closest_value is None or abs(arr[right] - target) < abs(closest_value - target):
                    closest_value = arr[right]
            return closest_value

        result = 0 
        arr2.sort()
        for a1 in arr1:
            if abs(binary_search(arr2,a1)-a1)>d:
                result+=1
        return result