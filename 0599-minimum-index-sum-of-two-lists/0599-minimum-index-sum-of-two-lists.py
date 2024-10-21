class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        Hash_map = {}
        result = []
        for i in range(len(list1)):
            if list1[i] in list2:
                Hash_map[list1[i]] = i+list2.index(list1[i])
        least_index_sum = min([v for v in Hash_map.values()])
        for k,v in Hash_map.items():
            print(k)
            if v == least_index_sum:
                result.append(k)
        return result
