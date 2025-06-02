# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # a1->a2->c1->c2->c3 -> b1->b2->b3->c1->c2->c3
        # b1->b2->b3->c1->c2->c3 -> a1->a2->c1->c2->c3

        currA = headA
        currB = headB
        
        while currA != currB:
            currA = currA.next if currA else headB
            currB = currB.next if currB else headA
        
        return currA