from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        s = [root]

        while s:
            n = s.pop()

            if n == None:
                break
        
            if n.left != None:
                if n.left.val >= n.val:
                    return False
                else:
                    s.append(n.left)

            if n.right != None:
                if n.right.val <= n.val:
                    return False
                else:
                    s.append(n.right)

        return True

            
