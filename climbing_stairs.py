class Solution(object):
    def fib(self, n, temp):
        if (n <= 1):
            temp[n] = 1
            return 1
   
        if(temp[n] != -1 ):
            return temp[n]
 
        temp[n] = self.fib(n - 1, temp) + self.fib(n - 2, temp)
        return  temp[n]
    
    
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        temp = [-1 for i in range(n + 1)]
        self.fib(n, temp)
        return temp[n]
