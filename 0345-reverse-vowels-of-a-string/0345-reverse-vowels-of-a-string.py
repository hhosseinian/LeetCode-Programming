class Solution:
    def reverseVowels(self, s: str) -> str:
        def isvowel(l:str):
            vowels = 'aeiou'
            return l.lower() in vowels
        l,r = 0,len(s)-1
        slist = list(s)
        while l<r:
            while l<r and not isvowel(slist[r]):
                #tmpr= s[r]+tmpr
                r-=1
            while l<r and not isvowel(slist[l]):
                #tmpl+=s[l]
                l+=1
            if l<r:
                slist[r],slist[l]=slist[l],slist[r]
                #tmpl +=s[r]
                #tmpr = s[l]+tmpr
            #elif l == r:
                #return tmpl+s[l]+tmpr
            l+=1
            r-=1
        return ''.join(slist)#tmpl+tmpr
