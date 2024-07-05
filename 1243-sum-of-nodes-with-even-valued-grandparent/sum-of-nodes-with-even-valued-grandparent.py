# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:

        output = 0

        def dfs(root, parent, grandparent):
            nonlocal output

            if root == None:
                return 0
            elif grandparent % 2 == 0:
                output+=root.val

            dfs(root.left, root.val, parent)
            dfs(root.right, root.val, parent)


        dfs(root.left, root.val, 1)
        dfs(root.right, root.val, 1)

        return output