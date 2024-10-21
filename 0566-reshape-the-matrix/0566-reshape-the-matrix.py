class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        Rows,Cols = len(mat),len(mat[0])
        if Rows*Cols !=r*c:
            return mat
        result = [[0]*c for _ in range(r)]
        for i in range(Rows):
            for j in range(Cols):
                flat_index = i*Cols+j
                result[flat_index//c][flat_index%c] = mat[i][j]
        return result