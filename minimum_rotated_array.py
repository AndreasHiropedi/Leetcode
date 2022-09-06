class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        if n == 1:
            return nums[0]
        
        elif n == 2:
            return min(nums[0], nums[1])
        
        else:
            return min(self.findMin(nums[:(n/2+1)]), self.findMin(nums[(n/2+1):]))
