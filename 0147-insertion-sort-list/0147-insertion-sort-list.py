# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # insertion sort linked list
        # return head of sorted list
        # list not empty
        if not head or not head.next:
            return head
        dummy = ListNode(0,head)
        prev, curr = head, head.next
        while curr:
            if curr.val >= prev.val:
                prev,curr = curr,curr.next
                continue
            temp = dummy.next
            # print(temp.val)
            if temp.val >= curr.val: # replace head
                dummy.next = curr
                curr_next = curr.next
                prev.next = curr_next
                curr.next = temp
                curr = prev.next
                continue
            # temp_prev = temp
            while temp.next.val < curr.val:
                # temp_prev = temp
                temp = temp.next
            # at this point, we need to insert curr after temp_prev 
            temp_next = temp.next
            curr_next = curr.next
            temp.next = curr
            curr.next = temp_next
            prev.next = curr_next
            curr = prev.next
        return dummy.next

    
        