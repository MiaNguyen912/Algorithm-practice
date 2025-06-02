# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        s,f = head, head
        tempHead = ListNode(0,head)
        prev = tempHead
        for i in range(n):
            f = f.next
        while f:
            prev = s
            s = s.next
            f = f.next
        # if s == head:
        #     return head.next
        prev.next = s.next
        return tempHead.next