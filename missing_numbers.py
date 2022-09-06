missing_nums = []
        n = len(nums)
        for i in range(1, n+1):
            if i not in nums:
                missing_nums.append(i)
        return missing_nums
