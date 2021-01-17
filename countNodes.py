# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        l = root
        r = root

        h_l = 0
        h_r = 0

        while l:
            h_l += 1
            l = l.left

        while r:
            h_r += 1
            r = r.right

        if h_l == h_r:
            return int(math.pow(2, h_l) - 1)

        return int(1 + self.countNodes(root.left) + self.countNodes(root.right))
