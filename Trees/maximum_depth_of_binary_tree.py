from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.d = 0

    def helper(self, root: Optional[TreeNode], d: int) -> None:
        if root == None:
            self.d = max(self.d, d)
            return

        d += 1

        self.helper(root.left, d)
        self.helper(root.right, d)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.helper(root, 0)

        return self.d