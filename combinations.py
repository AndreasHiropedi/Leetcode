from itertools import combinations

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if n == 1:
            return [[1]]
        
        nums = [i for i in range(1, n+1)]
        
        combs = list(combinations(nums, k))
        
        return combs
