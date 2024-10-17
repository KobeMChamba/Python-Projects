# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Initialize two pointers, slow and fast
        slow = head
        fast = head
        
        # Traverse the list with both pointers
        while fast and fast.next:
            slow = slow.next          # Move slow pointer by 1 step
            fast = fast.next.next     # Move fast pointer by 2 steps
            
            # If the two pointers meet, there is a cycle
            if slow == fast:
                return True
        
        # If fast reaches the end, there is no cycle
        return False