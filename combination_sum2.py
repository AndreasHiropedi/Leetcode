from itertools import combinations

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        nums = [1,2,3,4,5,6,7,8,9]
        
        combs = list(combinations(nums, k))
        
        good_combs = []
        
        for comb in combs:
            if sum(comb) == n:
                good_combs.append(comb)
        
        return good_combs
