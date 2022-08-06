# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # edge case root is None
        if root == None:
            return root

        # edge case left and right are None
        if root.left == None and root.right == None:
            return root

        # start recursion
        self.invertTreeHelper(root)

        return root

    def invertTreeHelper(self, node: Optional[TreeNode]):

        # swap left and right node
        rootTmp = node.left
        node.left = node.right
        node.right = rootTmp

        if node.left != None:
            self.invertTreeHelper(node.left)

        if node.right != None:
            self.invertTreeHelper(node.right)
