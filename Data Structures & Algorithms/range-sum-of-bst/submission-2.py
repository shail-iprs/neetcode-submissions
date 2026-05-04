# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.res=0

        def check(root):
            if not root:
                return 0
            check(root.left)
            if low<=root.val<=high:
                self.res+=root.val
            check(root.right)

        check(root)
        return self.res