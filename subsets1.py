class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        subs = [[]]
        
        for elem in nums:
            subs = subs + [sub + [elem] for sub in subs]
        
        return subs
