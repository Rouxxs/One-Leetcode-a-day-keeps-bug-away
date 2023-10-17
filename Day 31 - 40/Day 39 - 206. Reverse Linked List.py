# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Iterative solution
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        prev = None

        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        return prev

# Recursive solution
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        tmp = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return tmp


