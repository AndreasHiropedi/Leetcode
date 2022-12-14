class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        left = 0
        right = len(arr) - 1
 
        while right - left >= k:
            if abs(arr[left] - x) > abs(arr[right] - x):
                left = left + 1
            else:
                right = right - 1
 
        return arr[left:left + k]
