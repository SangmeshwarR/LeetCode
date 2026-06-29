# 111. Minimum Depth of Binary Tree

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        elif root.left is None and root.right is None:
            return 1 
        elif root.left is None:
            return 1 + self.minDepth(root.right)
        elif root.right is None:
            return 1 + self.minDepth(root.left)
        return 1+min(self.minDepth(root.left),self.minDepth(root.right))