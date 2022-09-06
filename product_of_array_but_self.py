import numpy as np

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = []
        for i in range(len(nums)):
            if i > 1:
                list1 = np.array(nums[:i])
                list2 = np.array(nums[(i+1):])
                product = np.prod(list1) * np.prod(list2)
                answer.append(int(product))
            elif i ==1: 
                list1 = np.array(nums[2:])
                product = nums[0] * np.prod(list1)
                answer.append(int(product))
            else:
                list1 = np.array(nums[1:])
                product = np.prod(list1)
                answer.append(int(product))
        return answer
