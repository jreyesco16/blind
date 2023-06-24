from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def helper(self, root: Optional[TreeNode]) -> List[int]:
        r = [] # result 
        s = [root] # stack

        while s:
            c = s.pop() # current
            
            if c == None:
                return

            r.append(c.val)

            if c.left != None:
                s.append(c.left)
            else:
                r.append(None)

            if c.right != None:
                s.append(c.right)

        return r
            

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_l = self.helper(p) # p traversed list
        q_l = self.helper(q) # q traversed list

        return p_l == q_l