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
        oldtoNew={None:None}

        curr=head

        while curr:
            new=Node(curr.val)
            oldtoNew[curr]=new
            curr=curr.next
        
        curr=head
        while curr:
            new=oldtoNew[curr]
            new.next=oldtoNew[curr.next]
            new.random=oldtoNew[curr.random]
            curr=curr.next
        
        return oldtoNew[head]