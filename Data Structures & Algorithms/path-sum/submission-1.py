# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def check(root,curr):
            if not root:
                return False
            
            if not root.left and not root.right and curr+root.val==targetSum:
                return True
            
            return check(root.left,curr+root.val) or check(root.right,curr+root.val)
        return check(root,0)
        