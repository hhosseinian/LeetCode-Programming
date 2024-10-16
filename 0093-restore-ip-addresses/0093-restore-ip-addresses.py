class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def isValid(segment)->bool:
            if not segment:
                return False
            if len(segment)>1 and segment[0]=='0':
                return False
            if 0<= int(segment) <=255:
                return True
            return False
        def backtrack(start: int, segments: int, current_ip: str)->int:
            if segments == 4:
                if start == len(s):
                    results.append(current_ip[:-1])
            for length in range(1,4):
                segment = s[start:start+length]
                if isValid(segment):
                    backtrack(start+length,segments+1,current_ip+segment+'.')
        results = []
        backtrack(0,0,'')
        return results