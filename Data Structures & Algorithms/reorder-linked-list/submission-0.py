# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if not head or not head.next:
            return

        def get_second_half(node):
            """Finds the midpoint and severs the first half from the second."""
            slow, fast = node, node
            prev = None
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            
            # This 'cuts' the list in two. 
            # For [2,4,6,8,10], first half becomes [2,4,6], second is [8,10]
            if prev:
                prev.next = None
            return slow

        def reverse_list(node):
            """Standard reversal: flips the direction of all pointers."""
            prev = None
            curr = node
            while curr:
                future = curr.next
                curr.next = prev
                prev = curr
                curr = future
            return prev

        def merge_lists(l1, l2):
            """Interleaves two lists until the second half is exhausted."""
            while l2 and l1:
                # Store the 'next' nodes before we break the links
                next_l1 = l1.next
                next_l2 = l2.next
                
                # Connect l1 to l2, then l2 to the rest of l1
                l1.next = l2
                if next_l1:
                    l2.next = next_l1
                
                # Step forward
                l1 = next_l1
                l2 = next_l2

        # Execution Pipeline
        mid = get_second_half(head)
        reversed_second = reverse_list(mid)
        merge_lists(head, reversed_second)
