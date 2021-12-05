# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        @lru_cache(maxsize=None)
        def getMoney(node, canRob):
            if not node: return 0
            money = 0
            if canRob:
                option1 = node.val
                option1 += getMoney(node.left, False) + getMoney(node.right, False)
                option2 = 0
                option2 += max(getMoney(node.left, True), getMoney(node.left, False))
                option2 += max(getMoney(node.right, True), getMoney(node.right, False))
                money = max(option1, option2)
            else:
                money += getMoney(node.left, True)
                money += getMoney(node.right, True)
            return money
        return getMoney(root, True)