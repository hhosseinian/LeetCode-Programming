class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        results = []
        def backtrack(start, current_combination, remaining):
            if remaining == 0:
                results.append(list(current_combination))
                return
            if remaining<0:
                return
            for i in range(start,len(candidates)):
                if i >start and candidates[i] == candidates[i-1]:
                    continue
                current_combination.append(candidates[i])
                backtrack(i+1,current_combination,remaining-candidates[i])
                current_combination.pop()
        backtrack(0,[],target)
        return results
