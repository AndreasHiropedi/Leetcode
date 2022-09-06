class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        indexes = [i for i,x in enumerate(matrix[m]) if x == 0]
                for k in range(len(matrix)):
                    for index in indexes:
                        matrix[k][index] = 0
                matrix[m] = [0] * no_of_columns
        """
        no_of_columns = len(matrix[0])
        
        contains_0 = []
        
        for m in range(len(matrix)):
            if 0 in matrix[m]:
                contains_0.append(True)         
            else:
                contains_0.append(False)
        
        for i in range(len(contains_0)):
            if contains_0[i]:
                indexes = [j for j,x in enumerate(matrix[i]) if x == 0]
                for k in range(len(matrix)):
                    for index in indexes:
                        matrix[k][index] = 0
                matrix[i] = [0] * no_of_columns
