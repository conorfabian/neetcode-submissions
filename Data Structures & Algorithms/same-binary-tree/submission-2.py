# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q1, q2 = [p], [q]

        while q1 and q2:
            curr1, curr2 = q1.pop(0), q2.pop(0)
            if not curr1 and not curr2:
                continue
            elif (curr1 and curr2 and curr1.val != curr2.val) or (not curr1 or not curr2):
                return False
            q1.append(curr1.left)
            q1.append(curr1.right)
            q2.append(curr2.left)
            q2.append(curr2.right)

        print(q1, q2)
        if q1 or q2:
            return False
        return True