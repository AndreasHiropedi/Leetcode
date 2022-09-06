# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        nodes = set()
        temp = head
        while (head):
            if (temp in nodes):
                return temp
            nodes.add(temp)
            if temp is not None:
                temp = temp.next
            else:
                return None
        return None
