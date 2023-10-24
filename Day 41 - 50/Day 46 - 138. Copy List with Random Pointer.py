"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashMap = {None : None}

        it = head
        while it:
            newNode = Node(it.val)
            hashMap[it] = newNode
            it = it.next
        
        it = head
        while it:
            newNode = hashMap[it]
            newNode.next = hashMap[it.next]
            newNode.random = hashMap[it.random]
            it = it.next

        return hashMap[head]