class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ('a', 'e', 'i', 'o', 'u')
        n = len(s)
        reverset_vowel_s_left =""
        reverset_vowel_s_right =""
        if n == 1:
            return s
        left,right = 0,n-1
        while left<=right:
            while(s[left].lower() not in vowels and left<right):
                reverset_vowel_s_left+= s[left]
                left+=1
            while(s[right].lower() not in vowels and left<right):
                reverset_vowel_s_right= s[right] + reverset_vowel_s_right
                right -=1
            if left<right:
                reverset_vowel_s_left+= s[right]
                reverset_vowel_s_right= s[left] + reverset_vowel_s_right
            else:
                reverset_vowel_s_left+= s[right]
            left+=1
            right -=1
        return reverset_vowel_s_left+reverset_vowel_s_right