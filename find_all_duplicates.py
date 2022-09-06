class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = list(set([i for i in nums if nums.count(i) > 1]))
        return result
