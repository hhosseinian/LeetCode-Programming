class Solution:
    from collections import deque
    def numSquares(self, n: int) -> int:
        perfect_square = []
        visited = set([n])
        i = 1
        while i*i<=n:
            perfect_square.append(i*i)
            i+=1
        queue = deque([(n,0)])
        
        while queue:
            curr_num,steps = queue.popleft()
            for square in perfect_square:
                next_num = curr_num-square
                if next_num<0:
                    break
                if next_num == 0:
                    return steps+1
                if next_num not in visited:
                    visited.add(next_num)
                    queue.append((next_num,steps+1))
        return -1
