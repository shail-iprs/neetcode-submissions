# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        dp={None:0}

        def dfs(root):
            if root in dp:
                return dp[root]

            res=root.val
            if root.left:
                res+=dfs(root.left.left)+dfs(root.left.right)
            if root.right:
                res+=dfs(root.right.left)+dfs(root.right.right)

            dp[root]=max(res,dfs(root.left)+dfs(root.right))
            return dp[root]
        return dfs(root)