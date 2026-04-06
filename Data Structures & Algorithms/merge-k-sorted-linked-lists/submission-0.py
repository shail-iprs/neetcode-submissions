# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def merge(h1,h2):
    dummy=ListNode()
    head=dummy

    while h1 and h2:
        if h1.val<=h2.val:
            dummy.next=h1
            h1=h1.next
            #dummy=dummy.next
        else:
            dummy.next=h2
            h2=h2.next
        dummy=dummy.next
    
    if h1:
        dummy.next=h1
    if h2:
        dummy.next=h2
    return head.next
        
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        if len(lists)==1:
            if lists[0]==None:
                return None
            else:
                return lists[0]
        
        first=lists[0]

        for ind in range(1,len(lists)):
            mergehead=merge(first,lists[ind])
            first=mergehead
        return first


