class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums[0], nums[1], nums[0] + nums[1])
        
        max_so_far = nums[0]
        curr_max = nums[0]
      
        for i in range(1,len(nums)):
            curr_max = max(nums[i], curr_max + nums[i])
            max_so_far = max(max_so_far,curr_max)
          
        return max_so_far
