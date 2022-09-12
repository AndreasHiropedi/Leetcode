import itertools

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 3:
            return sum(nums)
        
        all_combs = list(map(list, itertools.combinations(nums, 3)))
        diffs = []
        for item in all_combs:
            difference = abs(sum(item) - target)
            diffs.append(difference)
        best_diff = min(diffs)
        index = diffs.index(best_diff)
        
        return sum(all_combs[index])
