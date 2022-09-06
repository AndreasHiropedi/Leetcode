# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        q = [root]
        ans = []
        while len(q):
            qlen = len(q)
            row = 0
            for i in range(qlen):
                curr = q.pop(0)
                row = row + curr.val
                if curr.left: 
                    q.append(curr.left)
                if curr.right: 
                    q.append(curr.right)
            ans.append(row * 1.0 / qlen)
        return ans
