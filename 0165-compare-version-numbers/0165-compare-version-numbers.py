class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        n1 = len(version1)
        n2 = len(version2)
        ptr1,ptr2 =0,0
        while ptr1<n1 or ptr1<n2:
            segment1 = ''
            while ptr1<n1 and version1[ptr1]!='.':
                segment1+= version1[ptr1]
                ptr1+=1
            segment2 = ''
            while ptr2<n2 and version2[ptr2]!='.':
                segment2+= version2[ptr2]
                ptr2+=1
            v1 =int(segment1) if segment1 else 0
            v2 =int(segment2) if segment2 else 0
            if v1<v2:
                return -1
            elif v1>v2:
                return 1
            ptr1+=1
            ptr2+=1
        return 0
