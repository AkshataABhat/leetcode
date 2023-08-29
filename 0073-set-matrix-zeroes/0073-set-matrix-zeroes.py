class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        rs, cs = set(), set()
        
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    cs.add(j)
                    rs.add(i)
                    
        for r in rs:
            for j in range(cols):  # Fix: Iterate through columns
                matrix[r][j] = 0
                
        for c in cs:
            for i in range(rows):  # Fix: Iterate through rows
                matrix[i][c] = 0
