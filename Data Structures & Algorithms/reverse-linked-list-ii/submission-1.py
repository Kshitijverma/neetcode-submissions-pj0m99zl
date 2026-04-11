# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == 1:
            return self.reverseN(head, right)

        pre = head
        for _ in range(1, left - 1):
            pre = pre.next

        pre.next = self.reverseN(pre.next, right - left + 1)

        return head

    def reverseN(self, head, n):
        if head is None or head.next is None or n <= 1:
            return head 

        prev, curr = None, head
        
        while curr and n > 0:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            n -= 1

        head.next = curr
        
        return prev