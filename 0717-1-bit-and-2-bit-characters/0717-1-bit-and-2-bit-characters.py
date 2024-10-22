class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        n = len(bits)
        last_is_one_bit = False
        i = 0
        while i<n:
            if bits[i] == 1:
                i+=2
                last_is_one_bit = False
            else:
                last_is_one_bit = True
                i+=1
        return last_is_one_bit