class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 1. Handle edge cases
        if not head or not head.next:
            return head
            
        # 2. Find the length and the original tail
        length = 0
        count = head
        while count.next:
            length += 1
            count = count.next
        length += 1 # Account for the final node
        
        # 3. Optimize k
        k = k % length
        
        # 4. Locate the new tail
        p = head
        for _ in range(length - k - 1):
            p = p.next
            
        # 5 & 6. Form the circle, set new head, and break it
        count.next = head
        head = p.next
        p.next = None
        
        # 7. Return the new rotated list
        return head