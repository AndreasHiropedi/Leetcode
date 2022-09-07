# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        temp = head
        length = 0
 
        while (temp != None):
            length += 1
            temp = temp.next
        
        if length == 0:
            return head
        
        new_temp = head
        middle = length // 2
        while middle != 0:
                new_temp = new_temp.next
                middle -= 1
        return new_temp
