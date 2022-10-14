# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        s = [root]
        
        # traverse tree in MLR order
        while s:
            n = s.pop(0)

            if n.val==subRoot.val:
                if self.helper(n, subRoot):
                    return True
            
            if n.left:
                s.append(n.left)
                
            if n.right:
                s.append(n.right)
                
        return False
    
    def helper(self, root, subRoot):
        if not subRoot and not root:
            return True
        
        if not root or not subRoot:
            return False
        
        if root.val != subRoot.val:
            return False
        
        return self.helper(root.left, subRoot.left) and self.helper(root.right, subRoot.right)