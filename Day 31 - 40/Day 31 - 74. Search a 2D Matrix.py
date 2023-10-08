class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        top, bot = 0, m - 1
        while top <= bot:
            mid = top + (bot - top) // 2
            if matrix[mid][0] > target:
                bot = mid - 1
            elif matrix[mid][-1] < target:
                top = mid + 1
            else:
                break
        
        r = top + (bot - top) // 2
        left, right = 0, n - 1
        while left <= right:
            mid = left + (right - left) // 2
            if matrix[r][mid] > target:
                right = mid - 1
            elif matrix[r][mid] < target:
                left = mid + 1
            else:
                return True
        return False