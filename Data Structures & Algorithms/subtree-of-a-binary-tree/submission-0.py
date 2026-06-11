# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root or not subRoot:
            return
        elif root.val == subRoot.val:
            if self.equalTree(root, subRoot):
                return True

        if self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot):
            return True

        return False

    def equalTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        s1, s2 = [root], [subRoot]

        while s1 and s2:
            p, q = s1.pop(), s2.pop()
            if not p and not q:
                continue
            elif not p or not q or p.val != q.val:
                return False

            s1.append(p.right)
            s1.append(p.left)
            s2.append(q.right)
            s2.append(q.left)

        return len(s1) == len(s2)
