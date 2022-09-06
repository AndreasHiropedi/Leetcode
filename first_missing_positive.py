class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            if nums[0] != 1:
                return 1
            return 2
        
        max_number = max(nums)
        count = 1
        
        if max_number < 1:
            return 1
        
        while count <= max_number:
            if count in nums:
                count += 1
            else:
                return count
            
        return (max_number + 1)
