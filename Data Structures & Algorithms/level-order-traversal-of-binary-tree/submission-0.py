# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = [root]
        while q:
            n = len(q)
            level = []
            for i in range(n):
                curr = q.pop(0)
                if not curr:
                    continue
                level.append(curr.val)
                q.append(curr.left)
                q.append(curr.right)
            if level:
                res.append(level)

        return res