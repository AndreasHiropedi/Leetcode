class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums)
        
        prev2 = 0
        prev1 = 0
        for i in range(len(nums)):
            temp = prev1
            prev1 = max(prev2+nums[i],prev1)
            prev2 = temp
        return prev1
