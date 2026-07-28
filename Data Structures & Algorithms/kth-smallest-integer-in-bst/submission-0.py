# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        heap = []
        q = collections.deque([root])
        while q:
            curr = q.popleft()
            if not curr:
                continue
            heapq.heappush(heap, curr.val * -1)
            while len(heap) > k:
                heapq.heappop(heap)
            q.append(curr.left)
            q.append(curr.right)

        return heapq.heappop(heap) * -1