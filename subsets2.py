class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        subs = [[]]
        
        for elem in nums:
            subs = subs + [sub + [elem] for sub in subs]
        
        new_subs = []
        
        for element in subs:
            if element not in new_subs:
                new_subs.append(element)
        
        return new_subs
