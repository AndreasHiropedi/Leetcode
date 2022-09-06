"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        nodeMap = {}
        return self.cloneNode(node, nodeMap)
    
    def cloneNode(self, node, nodeMap):
        if node == None:
            return None
        if node.val in nodeMap:
            return nodeMap[node.val]
        newNode = Node(node.val)
        nodeMap[node.val] = newNode
        for neighbor in node.neighbors:
            newNode.neighbors.append(self.cloneNode(neighbor, nodeMap))
        return newNode
