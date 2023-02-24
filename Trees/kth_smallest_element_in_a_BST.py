# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        s = []

        c = root

        while k != 0:
            if c == None:
                break
            elif k == 1 and c.left == None:
                return c.val

            if c.left == None and c.right == None:
                k -= 1
                if s:
                    c = s.pop()
                    c.left = None
            elif c.left != None: 
                s.append(c)
                c = c.left
            else:
                k -= 1
                c = c.right
                    
        return 0