# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        from collections import deque

        dp = deque([p])
        dq = deque([q])

        while dp:
            cp = dp.popleft()
            cq = dq.popleft()

            if not cp and not cq:
                continue

            if not cp or not cq or cp.val != cq.val:
                return False

        
            dp.append(cp.left)
            dq.append(cq.left)

        
            dp.append(cp.right)
            dq.append(cq.right)
            
        return True
