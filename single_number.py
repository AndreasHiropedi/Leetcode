result = nums[0]
        for i in range(1, len(nums)):
            result = result ^ nums[i] 
        return result
