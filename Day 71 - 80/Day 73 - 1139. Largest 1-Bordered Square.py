class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        L, R = [g[:] for g in grid], [g[:] for g in grid]
        A, B = [g[:] for g in grid], [g[:] for g in grid]

        for i in range(len(grid)):
            for j in range(1, len(grid[0])):
                if L[i][j] : L[i][j] += L[i][j - 1]
            for j in range(len(grid[0])-2, -1,-1):
                if R[i][j] : R[i][j] += R[i][j + 1]
        
        for j in range(len(grid[0])):
            for i in range(1, len(grid)):
                if A[i][j] : A[i][j] += A[i-1][j]
            for i in range(len(grid)-2, -1,-1):
                if B[i][j] : B[i][j] += B[i+1][j]
                
        l = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                for k in range(min(L[i][j], A[i][j])):
                    if min(R[i - k][j-k], B[i - k][j - k]) >= k:
                        l = max(l, (k+1) * (k+1))
        
        return l