class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        N = len(gain)
        mx = max(0,gain[0])
        alt = gain[0]
        for i in range(1,N):
            alt += gain[i]
            mx =max(mx,alt)
        return mx
            
            
        