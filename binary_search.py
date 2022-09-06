class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        
        elif len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        
        low = 0
        high = len(nums) - 1
        
        while high - low > 1:
            mid = (low + high) // 2
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid
        
        if nums[low] == target:
            return low
        elif nums[high] == target:
            return high
        return -1
