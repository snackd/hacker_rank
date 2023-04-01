# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        depth = 0
        if root:
            level = [root]
        else:
            level = []

        while level:
            depth += 1
            next_level = []
            for element in level:
                if element.left:
                    next_level.append(element.left)
                if element.right:
                    next_level.append(element.right)
            level = next_level

        return depth

    # def maxDepth(self, root: Optional[TreeNode]) -> int:
    #     if not root:
    #         return 0

    #     return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    #  def maxDepth(self, root: Optional[TreeNode]) -> int:
    #     level = 0
    #     q = deque([root])

    #     while q:
    #         for i in range(len(q)):
    #             node = q.popleft()
    #             if node.left:
    #                 q.append(node.left)
    #             if node.right:
    #                 q.append(node.right)
    #         level += 1
    #     return level
