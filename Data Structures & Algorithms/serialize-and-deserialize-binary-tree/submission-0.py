# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.

    def serialize(self, root: Optional[TreeNode]) -> str:
        curr=[]
        q=deque([root])
        while q:
            node=q.popleft()
            if not node:
                curr.append('N')
                continue
            curr.append(str(node.val))
            q.append(node.left)
            q.append(node.right)
        return ",".join(curr)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data or data=='N':
            return None
        vals=data.split(',')
        ind=0
        root=TreeNode(int(vals[ind]))
        q=deque([root])

        while q:
            curr=q.popleft()
            ind+=1
            if ind<len(vals) and vals[ind]!='N':
                curr.left=TreeNode(int(vals[ind]))
                q.append(curr.left)
            ind+=1
            if ind<len(vals) and vals[ind]!='N':
                curr.right=TreeNode(int(vals[ind]))
                q.append(curr.right)
        return root










