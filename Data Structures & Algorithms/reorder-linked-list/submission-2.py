# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        temp = slow.next
        slow.next = prev = None
        slow = temp
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        l1, l2 = head, prev
        dummy = ListNode()
        curr = dummy
        while l1 and l2:
            curr.next = l1
            l1 = l1.next
            curr = curr.next
            curr.next = l2
            l2 = l2.next
            curr = curr.next

        if l1:
            curr.next = l1
        elif l2:
            curr.next = l2