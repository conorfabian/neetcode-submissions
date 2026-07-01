# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def sameTree(p, q):
            q1, q2 = collections.deque([p]), collections.deque([q])
            while q1 and q2:
                curr1, curr2 = q1.popleft(), q2.popleft()
                if not curr1 and not curr2:
                    continue
                elif (curr1 and curr2 and curr1.val != curr2.val) or (not curr1 or not curr2):
                    return False
                q1.append(curr1.left)
                q1.append(curr1.right)
                q2.append(curr2.left)
                q2.append(curr2.right)

            return True

        q = collections.deque([root])
        while q:
            curr = q.popleft()
            if not curr:
                continue
            elif sameTree(curr, subRoot):
                return True
            q.append(curr.left)
            q.append(curr.right)

        return False