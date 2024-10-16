class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        S= s.replace('-','').upper()
        print(S)
        N = len(S)
        frist_group_size = N%k if N%k != 0 else k
        result = S[:frist_group_size]
        for i in range(frist_group_size ,N,k):
            result += '-'+S[i:i+k]
        return result

