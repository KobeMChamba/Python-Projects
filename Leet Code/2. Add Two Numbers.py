# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize dummy node and current pointer for the result list
        dummy = ListNode(0)
        current = dummy
        
        carry = 0  # Carry will store the carry-over for addition
        
        # Traverse both linked lists
        while l1 or l2:
            # Get the values of the current nodes, if any (or 0 if one list is shorter)
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Add the two values together with the carry
            total = val1 + val2 + carry
            carry = total // 10  # Update carry for the next iteration
            current.next = ListNode(total % 10)  # Create the next node in the result
            
            # Move current pointer forward in result list
            current = current.next
            
            # Move to the next nodes in l1 and l2, if available
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        # After the loop, if there's any carry left, create a new node for it
        if carry > 0:
            current.next = ListNode(carry)
        
        # Return the result linked list, which starts at dummy.next
        return dummy.next

        
        