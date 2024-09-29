class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start,path,current_sum):
            if current_sum == target:
                result.append(path[:])
                return
            for i in range(start,len(candidates)):
                if candidates[i]+current_sum <= target:
                    path.append(candidates[i])
                    backtrack(i, path,candidates[i]+current_sum )
                    path.pop()
        result = []
        backtrack(0,[],0)
        return result


