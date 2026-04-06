"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_new={None:None}

        curr=head
        while curr:
            node=Node(curr.val)
            old_new[curr]=node
            curr=curr.next
        
        curr=head
        while curr:
            node=old_new[curr]
            node.next=old_new[curr.next]
            node.random=old_new[curr.random]
            curr=curr.next
        return old_new[head]
