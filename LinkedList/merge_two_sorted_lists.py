# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        root_node = ListNode()
        tmp_node = root_node

        node_1 = list1

        node_2 = list2

        while(True):


            # edge case
            if node_1 is None and node_2 is None:
                break

            # edge case
            if node_1 is None:
                tmp_node.next = node_2
                break

            # edge case
            if node_2 is None:
                tmp_node.next = node_1
                break

            if node_1.val > node_2.val:
                tmp_node.next = node_2
                node_2 = node_2.next
            else:
                tmp_node.next = node_1
                node_1 = node_1.next

            tmp_node = tmp_node.next

        return root_node.next