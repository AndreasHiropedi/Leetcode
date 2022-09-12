import itertools

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 3:
            if sum(nums) == 0:
                return [nums]
            else:
                return []
        
        all_combs = list((map(list, itertools.combinations(nums, 3))))
        possible_triplets = []
        for item in all_combs:
            item.sort()
            if sum(item) == 0 and item not in possible_triplets:
                possible_triplets.append(item)
        return possible_triplets
