# 104. Maximum Depth of Binary Tree

from git import Optional
class Solution:
    def maxDepth(self, root: Optional[Optional.TreeNode]) -> int:
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))        