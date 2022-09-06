# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        nodes = set()
        temp = head
        while (head):
            if (temp in nodes):
                return True
            nodes.add(temp)
            if temp is not None:
                temp = temp.next
            else:
                return False
        return False
