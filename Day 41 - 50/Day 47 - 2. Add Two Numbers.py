# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode(0, None)
        tmp = 0
        p = ans
        while l1 or l2:
            sumVal = 0
            if l1 != None:
                sumVal += l1.val
                l1 = l1.next
            if l2 != None:
                sumVal += l2.val
                l2 = l2.next
            sumVal += tmp
            tmp = 0 if sumVal < 10 else 1
            sumVal = sumVal if sumVal < 10 else sumVal - 10
            p.next = ListNode(sumVal, None)
            p = p.next
        if tmp == 1:
            p.next = ListNode(tmp, None)
        return ans.next