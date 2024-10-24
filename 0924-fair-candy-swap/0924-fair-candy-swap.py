class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        Alice_sum = sum(aliceSizes)
        Bob_sum = sum(bobSizes)
        diffAB_sum = (Alice_sum-Bob_sum)//2
        bob_set = set(bobSizes)
        for A in aliceSizes:
            B = A-diffAB_sum
            if B in bob_set:
                return [A,B]
