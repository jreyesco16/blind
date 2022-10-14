# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # traverse linked list
        s = []
        while head:            
            s.append(head)
            head = head.next
            
        # remove index
        index = len(s)-n
        
        # edge case remove first link
        if index == 0:
            if 1 < len(s):
                return s[1]
            else:
                return None
        # edge case remove last link
        if index == len(s)-1:
            if 1 < len(s):
                s[-2].next = None
                return s[0]
            else: 
                return None
            
        s[index-1].next = s[index+1]
        
        return s[0]