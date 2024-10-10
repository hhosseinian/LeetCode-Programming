class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hashmap_freq = {}
        for a in arr:
            if a in hashmap_freq:
                hashmap_freq[a]+=1
            else:
                hashmap_freq[a] = 1
        checked = set()
        for v in hashmap_freq.values():
            if v in checked:
                return False
            else:
                checked.add(v)
        return True

