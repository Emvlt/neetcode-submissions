# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)  # The anchor
        current = dummy
        carry = 0
        while l1 or l2 or carry:
            # Get the values. If a list is already exhausted, use 0 instead.
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate total and new carry
            total = val1 + val2 + carry
            carry = total // 10       # Integer division: 15 // 10 = 1, 8 // 10 = 0
            val = total % 10          # Modulo: 15 % 10 = 5, 8 % 10 = 8
            
            # Create and link the new node
            current.next = ListNode(val)
            current = current.next
            
            # Move pointers forward, but only if they haven't reached the end
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            
        return dummy.next

        
        