class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        squared_nums = []
        for num in nums:
            squared_nums.append(num**2)
        
        return sorted(squared_nums)
