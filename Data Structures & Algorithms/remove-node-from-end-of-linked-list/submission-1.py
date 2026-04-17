# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        N = 0
        current = head 
        while current:
            N += 1
            current = current.next

        i = 0
        phantom = ListNode(val=0, next = head)
        current = phantom
        while i < N-n:
            i += 1
            current = current.next

        if current.next:
            current.next = current.next.next

        return phantom.next