# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        m_d = 1
        def dfs(node):
            nonlocal m_d
            if not node:
                return 0
            l = dfs(node.left)
            r = dfs(node.right)
            m_d = max(max(l+1, r+1), m_d)
            return max(l, r) + 1
        dfs(root)
        return m_d