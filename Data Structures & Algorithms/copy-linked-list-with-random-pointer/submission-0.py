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
        original_to_copy = {}
        temp = head
        while temp:
            original_to_copy[temp] = Node(temp.val)
            temp = temp.next

        temp = head
        while temp:
            copy_node = original_to_copy[temp]
            copy_node.next = original_to_copy.get(temp.next)
            copy_node.random = original_to_copy.get(temp.random)
            temp = temp.next

        return original_to_copy.get(head)