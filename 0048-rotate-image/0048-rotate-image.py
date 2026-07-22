class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l = len(matrix)
        floor_val = l // 2
        l -= 1
        
        
        for i in range(0, floor_val):
            for j in range(i, l - i):
                coord = [i, j]
                val = matrix[i][j]
                run_loop = True
                
                
                while run_loop:
                    temp = matrix[coord[1]][l - coord[0]]
                    coord[0], coord[1] = coord[1], l - coord[0]
                    matrix[coord[0]][coord[1]] = val
                    val = temp
                    
                    
                    if coord[0] == i and coord[1] == j:
                        run_loop = False