class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if target < matrix[i][j]:
                    break
                elif target == matrix[i][j]:
                    return True
        return False
