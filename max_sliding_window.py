class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return nums
        
        if len(nums) <= k:
            return [max(nums)]
        
        max_window = []
        for i in range(len(nums) - k + 1):
            temp = nums[i:(i+k)]
            max_window.append(max(temp))
        
        return max_window
