# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False

        visited = {}
        node = head

        while node.next:
            if node in visited:
                return True
            visited[node] = True
            node = node.next

        return False