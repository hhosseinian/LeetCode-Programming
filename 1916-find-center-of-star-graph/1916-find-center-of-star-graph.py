class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        n = len(edges)
        count_dict = {}
        for e in edges:
            if e[0] in count_dict:
                count_dict[e[0]]+=1
            else:
                count_dict[e[0]]=1
            if e[1] in count_dict:
                count_dict[e[1]]+=1
            else:
                count_dict[e[1]]=1
        for k,v in count_dict.items():
            if v == n:
                return k
        