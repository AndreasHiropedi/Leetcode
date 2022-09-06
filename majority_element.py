class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        vals = list(set(nums))
        counts = [0] * len(vals)
        
        for i in range(len(vals)):
            count = 0
            for num in nums:
                if num == vals[i]:
                    count = count + 1
            counts[i] = count
        
        index = counts.index(max(counts))
        
        return vals[index]
