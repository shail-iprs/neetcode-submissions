# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.curr=0

        def check(root):
            if not root:
                return

            if low<=root.val<=high:
                self.curr+=root.val
            check(root.left)
            check(root.right)
        check(root)
        return self.curr