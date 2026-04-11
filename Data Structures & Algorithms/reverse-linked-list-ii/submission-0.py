# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:
            return None
        
        def reverse(h1):
            prev=None
            curr=h1

            while curr:
                next_node=curr.next
                curr.next=prev
                prev=curr
                curr=next_node
            return prev
        prev=head
        prev_list=None
        for _ in range(left-1):
            prev_list=prev
            prev=prev.next
        clip_head=prev
        clip_tail=clip_head

        for _ in range(right-left):
            clip_tail=clip_tail.next
        
    
        next_list=clip_tail.next
        clip_tail.next=None

        reverse_list=reverse(clip_head)
        if prev_list:
            prev_list.next=reverse_list
        else:
            head=reverse_list
        clip_head.next=next_list
        return head
        

