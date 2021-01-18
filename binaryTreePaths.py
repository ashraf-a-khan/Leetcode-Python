# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if root is None:
            return []
        if not root.left and not root.right:
            return [str(root.val)]

        paths = self.binaryTreePaths(root.left) + self.binaryTreePaths(root.right)

        return ["{}->{}".format(root.val, path) for path in paths]