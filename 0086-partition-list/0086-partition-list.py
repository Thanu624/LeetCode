class Solution:    
    def partition(self, head: ListNode, k: int) -> ListNode:
    
        if not head: return None           
        less, more = ListNode(), ListNode()         # <-- 1
        lNode, mNode = less, more
        
        while head :                                # <-- 2                 
            if head.val < k :
                lNode.next = head
                lNode = lNode.next
            else:
                mNode.next = head
                mNode = mNode.next
            head=head.next

        lNode.next, mNode.next = more.next, None    

        return less.next                            