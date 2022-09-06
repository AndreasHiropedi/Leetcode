from itertools import combinations

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if sum(candidates) < target:
            return []
        
        if len(candidates) == 1:
            if candidates[0] == target:
                return [candidates]
            return []
        
        if len(candidates) == 2:
            if sum(candidates) == target:
                return [candidates]
            elif candidates[0] == target:
                return [[candidates[0]]]
            elif candidates[1] == target:
                return [[candidates[1]]]
            return []
        
        combs = []
        
        all_possible_combs = []
        
        for i in range(1, len(candidates)):
            all_possible_combs += list(combinations(candidates, i))
        
        for combination in all_possible_combs:
            if sum(combination) == target:
                comb = list(combination)
                comb.sort()
                if comb not in combs:
                    combs.append(comb)
                    
        return combs
