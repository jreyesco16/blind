from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        a = []

        def dfs(root: Optional[TreeNode], depth: int):
            # edge case
            if root == None:
                return

            if len(a) <= depth:
                a.append([])
            
            a[depth].append(root.val)

            if root.left != None:
                dfs(root.left, depth+1)
            
            if root.right != None:
                dfs(root.right, depth+1)

        dfs(root, 0)

        return a
