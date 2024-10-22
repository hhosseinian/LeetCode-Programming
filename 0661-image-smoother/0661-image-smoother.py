class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        Rows,Cols = len(img),len(img[0])
        Result = [[0]*Cols for _ in range(Rows)]
        directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        for i in range(Rows):
            for j in range(Cols):
                in_matrix_count = 1
                smoother_sum = img[i][j]
                for dr,dc in directions:
                    nr,nc = i+dr,j+dc
                    if 0<=nr<Rows and 0<=nc<Cols:
                        in_matrix_count+=1
                        smoother_sum += img[nr][nc]
                Result[i][j] = smoother_sum//in_matrix_count
        return Result


