from collections import deque
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        rows,cols = len(rooms),len(rooms[0])
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        queue = deque([])
        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    queue.append((r,c,0)) #x,y,distance from gate
        while queue:
            x,y,distance = queue.popleft()
            for dr,dc in directions:
                nr,nc=x+dr,y+dc
                if 0<=nr<rows and 0<=nc<cols and rooms[nr][nc] == 2147483647:
                    queue.append((nr,nc,distance+1))
                    rooms[nr][nc]=distance+1

            