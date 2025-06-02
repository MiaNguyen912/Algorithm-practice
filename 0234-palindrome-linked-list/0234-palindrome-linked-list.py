# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def findMiddle(head):
            s,f = head, head
            prev = head
            while f and f.next:
                prev = s
                s = s.next
                f = f.next.next
            prev.next = None # cut the list 
            return s
        
        def reverse(head):
            if not head or not head.next:
                return head
            prev,s,f = None,head, head.next
            while f:
                temp = f.next
                f.next = s
                s.next = prev

                prev = s
                s = f
                f = temp
            return s

        def printList(head):
            l = []
            while head:
                l.append(head.val)
                head = head.next
            print(l)

        mid = findMiddle(head)
        # printList(head) # [1,2]
        # printList(mid) # [2,1]
        second_head = reverse(mid)
        # printList(second_head) # [1,2]
        while head and second_head:
            if head.val != second_head.val:
                return False
            head = head.next
            second_head = second_head.next
        return True