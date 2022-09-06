# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        mergedList = ListNode()
        
        if list1 is None and list2 is None:
            return None
        
        elif list1 is None:
            return list2
        
        elif list2 is None:
            return list1
        
        merged = mergedList
        while True:     
            if list1 is None:
                merged.next = list2
                break
            elif list2 is None:
                merged.next = list1
                break
            if list1.val <= list2.val:
                merged.next = list1
                list1 = list1.next
            else:
                merged.next = list2
                list2 = list2.next
            merged = merged.next
        
        return mergedList.next
    
