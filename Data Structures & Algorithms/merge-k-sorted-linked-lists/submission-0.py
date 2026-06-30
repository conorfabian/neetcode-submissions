# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy= ListNode()
        curr = dummy
        while lists:
            minNode, minIdx = None, 0
            for i, node in enumerate(lists):
                if not minNode or minNode.val > node.val:
                    minNode = node
                    minIdx = i
            curr.next = minNode
            curr = curr.next
            lists[minIdx] = lists[minIdx].next
            if not lists[minIdx]:
                lists.pop(minIdx)

        return dummy.next