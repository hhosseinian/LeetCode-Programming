class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        def get_board_index(square):
            r = (square-1)//n
            c = (square-1)%n
            if r%2 ==1:
                c = n-1-c
            return n-1-r,c
        queue = deque([1])
        visited = set()
        visited.add(1)
        moves = 0
        while queue:
            for _ in range(len(queue)):
                curr =queue.popleft()
                if curr == n*n:
                    return moves
                for die_roll in range(1,7):
                    nxt_sq = curr+die_roll
                    if nxt_sq > n*n:
                        continue
                    row,col = get_board_index(nxt_sq)
                    if board[row][col] != -1:
                        nxt_sq = board[row][col]
                    if nxt_sq not in visited:
                        visited.add(nxt_sq)
                        queue.append(nxt_sq)
            moves+=1
        return -1

