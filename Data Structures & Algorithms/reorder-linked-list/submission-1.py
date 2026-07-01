# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next # start of second half
        prev = slow.next = None # cutting the first half off
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        dummy = ListNode()
        curr = dummy
        l1, l2 = head, prev
        while l1 and l2:
            curr.next = l1
            curr = l1
            l1 = l1.next
            curr.next = l2
            curr = l2
            l2 = l2.next
        curr.next = l1
        
        head = dummy.next
        return