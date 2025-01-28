class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head):
        # Create a dummy node
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        while head and head.next:
            # Identify the two nodes to swap
            first = head
            second = head.next
            
            # Perform the swap
            prev.next = second
            first.next = second.next
            second.next = first
            
            # Move the pointers for the next pair
            prev = first
            head = first.next
        
        # Return the new head of the list
        return dummy.next
