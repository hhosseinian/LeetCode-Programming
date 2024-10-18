from collections import defaultdict
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n ==1:
            return [0]
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        leaves = deque([i for i in range(n) if len(graph[i])==1])
        while n>2:
            n-=len(leaves)
            for _ in range(len(leaves)):
                leaf = leaves.popleft()
                neighbor =graph[leaf].pop()
                graph[neighbor].remove(leaf)
                if len(graph[neighbor]) == 1:
                    leaves.append(neighbor)
        return list(leaves)