# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        answer = float('-inf')
        def dfs(node):
            nonlocal answer
            if not node: return 0
            leftPath = dfs(node.left)
            rightPath = dfs(node.right)
            answer = max(answer, node.val + max(leftPath, rightPath, leftPath+rightPath, 0))
            return max(0, node.val+leftPath, node.val+rightPath, node.val)
        dfs(root)
        return answer