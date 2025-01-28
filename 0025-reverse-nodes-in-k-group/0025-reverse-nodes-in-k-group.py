class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head, k):
        # Step 1: Count the number of nodes in the list
        count = 0
        node = head
        while node:
            count += 1
            node = node.next
        
        # Step 2: Reverse in groups of k
        dummy = ListNode(0)
        dummy.next = head
        prev_group_end = dummy
        while count >= k:
            group_start = prev_group_end.next
            group_end = group_start
            # Find the end of the group
            for _ in range(k - 1):
                group_end = group_end.next
            
            # Save the next group start (after the current group)
            next_group_start = group_end.next
            
            # Reverse the current group
            prev, curr = None, group_start
            while curr != next_group_start:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            
            # Connect the previous group to the current reversed group
            prev_group_end.next = prev
            group_start.next = next_group_start
            prev_group_end = group_start
            
            # Reduce the count by k since we've processed a group
            count -= k
        
        return dummy.next
