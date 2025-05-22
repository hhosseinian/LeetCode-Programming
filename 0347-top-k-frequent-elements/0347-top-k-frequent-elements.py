class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            if n not in count:
                count[n]=1
            else:
                count[n]+=1
        items = list(count.items())
        n = len(items)
        result = []
        for i in range(k):
            max_indx = i
            for j in range(i+1,n):
                if items[j][1]>items[max_indx][1]:
                    max_indx = j
            items[max_indx],items[i]=items[i],items[max_indx]
            result.append(items[i][0])
        return result


