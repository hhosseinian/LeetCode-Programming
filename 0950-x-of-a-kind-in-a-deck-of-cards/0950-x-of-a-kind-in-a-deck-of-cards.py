from collections import Counter, defaultdict
from functools import reduce
import math
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        card_freq = Counter(deck)
        return reduce(math.gcd,card_freq.values()) >1