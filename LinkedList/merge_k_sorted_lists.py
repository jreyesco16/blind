# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        root = ListNode()

        d = {}

        while lists:
            c = lists.pop(0)

            # print("c", c)

            if c == None:
                continue

            if c.val in d:
                d[c.val].next = c
                lists.append(c.next)
                d[c.val].next.next = None
            else:
                d[c.val] = c
                lists.append(c.next)
                d[c.val].next = None

        keys = list(d.keys())

        keys.sort()

        s = root

        for k in keys:
            print("d[k]", d[k])
            s.next = d[k]

            while s.next !=None:
                s=s.next

        return root.next
