# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        l=[]
        while temp:
            l.append(temp.val)
            temp=temp.next
        c=Counter(l)
        l2=[i for i in c if c[i]==1]
        temp=head
        if not l2:
            return None
        for i in l2:
            temp.val=i
            prev=temp
            temp=temp.next
        prev.next=None
        return head