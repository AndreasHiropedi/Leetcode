class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # Create a 2D table to store
        # results of subproblems
        # one-liner logic to take input for rows and columns
        # mat = [[int(input()) for x in range (C)] for y in range(R)]
     
        count = [[0 for x in range(n)] for y in range(m)]
   
        # Count of paths to reach any
        # cell in first column is 1
        for i in range(m):
            count[i][0] = 1;
   
        # Count of paths to reach any
        # cell in first column is 1
        for j in range(n):
            count[0][j] = 1;
   
        # Calculate count of paths for other
        # cells in bottom-up
        # manner using the recursive solution
        for i in range(1, m):
            for j in range(1, n):            
                count[i][j] = count[i-1][j] + count[i][j-1]
                
        return count[m-1][n-1]
