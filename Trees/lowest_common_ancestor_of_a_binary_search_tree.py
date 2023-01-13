# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # current 
        c = root

        print("c", c)

        while c:
            if p.val > c.val and q.val > c.val:
                c = c.right
            elif p.val < c.val and q.val < c.val:
                c = c.left
            else:
                return c