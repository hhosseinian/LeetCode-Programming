from collections import defaultdict
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hashmap_freq = defaultdict(int)
        for a in arr:
                hashmap_freq[a]+=1
        checked = set()
        for v in hashmap_freq.values():
            if v in checked:
                return False
            else:
                checked.add(v)
        return True

