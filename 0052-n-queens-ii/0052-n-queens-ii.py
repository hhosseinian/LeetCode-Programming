class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(row: int, columns: set, diagonals1: set, diagonals2: set) -> int:
            if row == n:
                return 1

            count = 0
            for col in range(n):
                # Check if the column or the diagonals are under attack
                if col in columns or (row - col) in diagonals1 or (row + col) in diagonals2:
                    continue
                
                # Place the queen
                columns.add(col)
                diagonals1.add(row - col)
                diagonals2.add(row + col)

                # Move to the next row
                count += backtrack(row + 1, columns, diagonals1, diagonals2)

                # Remove the queen (backtrack)
                columns.remove(col)
                diagonals1.remove(row - col)
                diagonals2.remove(row + col)

            return count

        return backtrack(0, set(), set(), set())
