class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        Rows,Cols = len(mat),len(mat[0])
        if Rows*Cols !=r*c:
            return mat
        flat_list = [item for row in mat for item in row]
        result = [[0]*c for _ in range(r)]
        for i in range(r*c):
            result[i//c][i%c] = flat_list[i]
        return result