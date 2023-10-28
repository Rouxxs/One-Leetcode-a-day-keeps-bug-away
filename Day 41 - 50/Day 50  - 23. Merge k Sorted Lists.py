# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        
        while len(lists) > 1:
            merge = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                merge.append(self.mergeList(l1, l2))
            lists = merge
        return lists[0]

    def mergeList(self, l1, l2):
        if not l2:
            return l1
        small, big = (l1, l2) if l1.val < l2.val else (l2, l1)
        small.next = self.mergeList(small.next, big)
        return small