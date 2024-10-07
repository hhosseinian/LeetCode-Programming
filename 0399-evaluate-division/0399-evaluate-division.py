from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        for (a,b),value in zip(equations,values):
            graph[a][b] = value
            graph[b][a] = 1/value
        def dfs(start,end,visited):
            if start == end:
                return 1
            visited.add(start)
            for neighbor,value in graph[start].items():
                if neighbor not in visited:
                    product = dfs(neighbor,end,visited)
                    if product!=-1:
                        return product*value
            return -1
        results = []
        for a,b in queries:
            if a in graph and b in graph:
                result = dfs(a,b,set())
            else: 
                result = -1
            results.append(result)
        return results


        
        