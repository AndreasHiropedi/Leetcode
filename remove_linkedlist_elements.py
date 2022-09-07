# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head is None:
            return head
        
        # Store head node
        temp = head
        prev = None
  
        # If head node itself holds the key
        # or multiple occurrences of key
        while (temp != None and temp.val == val):
            head = temp.next  # Changed head
            temp = head         # Change Temp
  
        # Delete occurrences other than head
        while (temp != None):
  
            # Search for the key to be deleted,
            # keep track of the previous node
            # as we need to change 'prev.next'
            while (temp != None and temp.val != val):
                prev = temp
                temp = temp.next
  
            # If key was not present in linked list
            if (temp == None):
                return head
  
            # Unlink the node from linked list
            prev.next = temp.next
  
            # Update Temp for next iteration of outer loop
            temp = prev.next
        
        return head
