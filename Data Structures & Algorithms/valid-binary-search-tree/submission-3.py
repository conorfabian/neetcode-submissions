# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        q = deque([(root, float("-inf"), float("inf"))])
        while q:
            node, minVal, maxVal = q.popleft()
            if node.val >= maxVal or node.val <= minVal:
                return False
                
            if node.left:
                q.append((node.left, minVal, node.val))
            if node.right:
                q.append((node.right, node.val, maxVal))

        return True