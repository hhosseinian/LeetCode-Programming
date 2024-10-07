from collections import defaultdict, deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        for course,prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course]+=1
        queue = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)
        order = []
        while queue:
            course = queue.popleft()
            order.append(course)
            for neighbor in graph[course]:
                in_degree[neighbor]-=1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        if len(order) == numCourses:
            return order
        else:
            return []