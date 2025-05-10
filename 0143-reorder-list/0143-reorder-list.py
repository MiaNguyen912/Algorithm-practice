# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # use s, f to find the mid point of list -> then we'll merge the first haft and the reversed second haft
        # -> O(n) time, O(1) space
        if not head or not head.next or not head.next.next: # if list has <=2 nodes
            return head
        s,f = head, head
        while f and f.next:
            s = s.next
            f = f.next.next
        # at this point, s is at the mid point

        def reversed(head:ListNode):
            if not head or not head.next:
                return head
            prev,curr = head, head.next
            head.next = None
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev

        # def printList(head):
        #     output = []
        #     while head:
        #         output.append(head.val)
        #         head = head.next
        #     print(output)

        reversed_second_half = reversed(s)
        # printList(reversed_second_half) # if list = [1,2,3,4] -> first_haft = [1,2,3], reversed_second_half=[4,3]
        # printList(head)

        s,f = head, reversed_second_half
        while f:
            f_next,s_next = f.next,s.next
            s.next = f
            f.next = s_next
            s = s_next
            f = f_next
            if f and not f.next:
                s.next = None

            # if s.next and not s.next.next:
            #     s.next = None
            #     break
        # printList(head)
        
        