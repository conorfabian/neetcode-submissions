# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        s1, s2 = [p], [q]

        while s1 and s2:
            p, q = s1.pop(), s2.pop()

            if not p and not q:
                continue
            elif not p or not q:
                return False
            elif p.val != q.val:
                return False

            s1.append(p.left)
            s1.append(p.right)
            s2.append(q.left)
            s2.append(q.right)

        return True