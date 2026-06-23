# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = list1, list2
        dummy = ListNode()
        curr = dummy
        while p1 and p2:
            if p1.val < p2.val:
                curr.next = p1
                temp = p1.next
                p1.next = None
                curr = p1
                p1 = temp
            else:
                curr.next = p2
                temp = p2.next
                p2.next = None
                curr = p2
                p2 = temp
        
        if p1:
            curr.next = p1
        elif p2:
            curr.next = p2

        return dummy.next
