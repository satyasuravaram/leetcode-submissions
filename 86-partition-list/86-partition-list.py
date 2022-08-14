# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head: return None
        if not head.next:
            return head
        a_start = None
        b_start = None
        nhead = ListNode(-69)
        nhead.next = head
        cur = nhead
        while cur and cur.next:
            if cur.next.val >= x:
                a_start = cur
                b_start = cur.next
                break
            cur = cur.next
        
        if not a_start:
            return head
        
        a_cur = a_start
        b_cur = b_start
        while b_cur and b_cur.next:
            if b_cur.next.val < x:
                a_cur.next = b_cur.next
                b_cur.next = b_cur.next.next                
                if a_cur.next:
                    a_cur.next.next = None
                a_cur = a_cur.next
            else:
                b_cur = b_cur.next
        
        a_cur.next = b_start
        return nhead if nhead.val != -69 else nhead.next