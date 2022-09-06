import numpy as np

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return nums[0]
         
        numbers = np.array(nums)
        max_product = np.prod(numbers)
        
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                number = np.array(nums[i:(j+1)])
                if np.prod(number) > max_product:
                    max_product = np.prod(number)
        
        if max(nums) > max_product:
            return max(nums)
            
        return max_product
