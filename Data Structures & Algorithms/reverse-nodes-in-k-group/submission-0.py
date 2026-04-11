# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        a = b = head
        for _ in range(k):
            if b is None:
                return head
            b = b.next

        newHead = self.reverseN(a,k)
        a.next = self.reverseKGroup(b,k)

        return newHead
    
    def reverseN(self, head, n):
        if head is None or head.next is None:
            return head 
        
        curr, prev = head, None

        while curr and n > 0:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
            n -= 1
        
        head.next = tmp

        return prev