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
        
        while currA and currB:
            if not currA and not currB:
                return None
            elif currA == currB:
                return currA

            currA = currA.next
            currB = currB.next
            
            if not currA and not currB:
                return None
            elif currA == currB:
                return currA

            if not currA: # reach the end -> go to next list
                currA = headB
            if not currB: # reach the end -> go to next list
                currB = headA
            
        # currA: 2 6 4      1 4 
        # currB: 1 5 None 2 6 5