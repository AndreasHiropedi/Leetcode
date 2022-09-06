class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_xor = -999999
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] ^ nums[j] > max_xor:
                    max_xor = nums[i] ^ nums[j]
        return max_xor
