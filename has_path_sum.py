# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if root is None:
            return False
        
        answer = False
        subSum = targetSum - root.val
        
        if subSum == 0 and root.left is None and root.right is None:
            return True
        
        if root.left is not None:
            answer = answer or self.hasPathSum(root.left, targetSum - root.val)
        
        if root.right is not None:
            answer = answer or self.hasPathSum(root.right, targetSum - root.val)
            
        return answer
