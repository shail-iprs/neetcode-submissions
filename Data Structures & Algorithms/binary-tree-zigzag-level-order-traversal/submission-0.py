# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        res=[]

        q=deque([root])
        flag=False

        while q:
            n=len(q)
            temp=[0]*n

            for ind in range(n):
                node=q.popleft()

                idx=ind if not flag else n-1-ind
                temp[idx]=node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            flag=not flag
            res.append(temp)
        return res
        

