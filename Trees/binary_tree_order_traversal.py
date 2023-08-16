from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        l = []
        q = [root]

        while q:
            level = []

            for i in range(len(q)):
                c = q.pop(0)

                if c:
                    level.append(c.val)
                    q.append(c.left)
                    q.append(c.right)


            if level: l.append(level)
                
        return l