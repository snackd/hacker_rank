# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __init__(self):
        self.result = 0

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.result = root.val
        self.dfs(root)
        return self.result

    def dfs(self, n: Optional[TreeNode]) -> int:
        if n.left:
            left = self.dfs(n.left)
        else:
            left = 0

        if n.right:
            right = self.dfs(n.right)
        else:
            right = 0

        max_value = max(n.val, left + n.val, right + n.val)
        self.result = max(self.result, max_value, left + right + n.val)
        return max_value
