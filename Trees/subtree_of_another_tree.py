from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def helper(self, r: Optional[TreeNode], subRoot: Optional[TreeNode]):
        if r == None and subRoot == None:
            return True
        if r == None and subRoot != None:
            return False
        if r != None and subRoot == None:
            return False
        if r.val != subRoot.val:
            return False

        return self.helper(r.left, subRoot.left) and self.helper(r.right, subRoot.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        s = [root] # set

        while s:
            c = s.pop() # current

            if c == None:
                return False

            if self.helper(c, subRoot):
                return True

            if c.left != None:
                s.append(c.left)

            if c.right != None:
                s.append(c.right)