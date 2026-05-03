# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter=0

        def get_res(root):
            if not root:
                return 0

            left=get_res(root.left)
            right=get_res(root.right)
            self.diameter=max(self.diameter,left+right)
            return 1+max(left,right)
        get_res(root)
        return self.diameter