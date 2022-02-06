# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        
        output = []
        to_delete = set(to_delete)
        def dfs(node, parent):
            if not node:
                return
            if node.val in to_delete:
                if parent:
                    if parent.left and parent.left.val == node.val:
                        parent.left = None
                    if parent.right and parent.right.val == node.val:
                        parent.right = None
                dfs(node.left, None)
                dfs(node.right, None)
            else:
                if not parent:
                    output.append(node)
                dfs(node.left, node)
                dfs(node.right, node)
        
        dfs(root, None)
        return output