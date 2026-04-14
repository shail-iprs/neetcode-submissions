# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        import math

        if not head:
            return None
        

        
        curr=head
        while curr.next:
            prev=curr
            nxt=curr.next
            gcd=math.gcd(curr.val,curr.next.val)
            temp=ListNode(gcd)
            prev.next=temp
            temp.next=nxt
            curr=curr.next.next
            
        return head

