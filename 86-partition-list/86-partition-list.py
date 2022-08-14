# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head or not head.next: 
            return head
        
        a_start, b_start = None, None
        dummy_head = ListNode(101)
        dummy_head.next = head
        cur = dummy_head
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
        if dummy_head.val == 101:
            dummy_head = dummy_head.next
            
        return dummy_head