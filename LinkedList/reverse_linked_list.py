from typing import Optional
import copy

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = copy.copy(head)

        reversed_nodes = None

        while n != None:
            tmpNode = reversed_nodes

            reversed_nodes = copy.copy(n)
            reversed_nodes.next = copy.copy(tmpNode)

            n = copy.copy(n.next)

        return reversed_nodes

    def formatNodes(self, l: list[int]) -> Optional[ListNode]:
        root = ListNode()

        node = root

        for x in l:

            node.next = ListNode(val=x)

            node = node.next

        return root.next


def main():
    test_case = [1, 2, 3, 4, 5]

    test_case_nodes = Solution().formatNodes(test_case)

    expected = Solution().formatNodes([5, 4, 3, 2, 1])

    result = Solution().reverseList(test_case_nodes)

    while expected != None:

        if expected.val != result.val:
            print("FAILED")
            return

        expected = expected.next
        result = result.next

    print("PASSED")


if __name__ == "__main__":
    main()
