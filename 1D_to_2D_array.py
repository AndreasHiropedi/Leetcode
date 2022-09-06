class Solution(object):
    def construct2DArray(self, original, m, n):
        """
        :type original: List[int]
        :type m: int
        :type n: int
        :rtype: List[List[int]]
        """
        if len(original) == 0:
            return [[]]
        if m*n != len(original):
            return []
        array2D = []
        counter = 0
        for i in range(m):
            array_temp = []
            for j in range(n):
                array_temp.append(original[counter])
                counter = counter + 1
            array2D.append(array_temp)
        return array2D
