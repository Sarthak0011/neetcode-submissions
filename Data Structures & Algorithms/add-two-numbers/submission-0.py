# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode(-1)
        temp = ans
        carry = 0
        while l1 and l2:
            sum = l1.val + l2.val + carry
            curr = None
            if sum >= 10:
                curr = ListNode(sum % 10)
                carry = 1
            else:
                curr = ListNode(sum)
                carry = 0
            temp.next = curr
            temp = temp.next
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            sum = l1.val + carry
            curr = None
            if sum >= 10:
                curr = ListNode(sum % 10)
                carry = 1
            else:
                curr = ListNode(sum)
                carry = 0
            temp.next = curr
            temp = temp.next
            l1 = l1.next

        while l2:
            sum = l2.val + carry
            curr = None
            if sum >= 10:
                curr = ListNode(sum % 10)
                carry = 1
            else:
                curr = ListNode(sum)
                carry = 0
            temp.next = curr
            temp = temp.next
            l2 = l2.next
        
        if carry:
            curr = ListNode(carry)
            temp.next = curr
        
        return ans.next