class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        n = len(timeSeries)
        if duration ==0:
            return 0
        total_P_time = 0
        for i in range(1,n):
            total_P_time+=min(duration,timeSeries[i]-timeSeries[i-1])
        total_P_time += duration # Add theduration of last event
        return total_P_time

