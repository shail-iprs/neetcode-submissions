# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        q=deque([(root,root.val)])
        total=0
        while q:
            node,curr=q.popleft()

            if not node.left and not node.right:
                total+=curr
            if node.left:
                q.append((node.left,10*curr+node.left.val))
            
            if node.right:
                q.append((node.right,10*curr+node.right.val))
        return total
