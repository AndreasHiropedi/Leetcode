class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        duplicate = 0
        
        for i in range(len(nums)-1):
            duplicate = nums[i]
            for j in range(i+1, len(nums)):
                if duplicate == nums[j]:
                    return duplicate
        return -1 
