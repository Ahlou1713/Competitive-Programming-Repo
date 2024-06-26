# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is not None:
            if (root.val >= p.val and root.val <= q.val) or (root.val >= q.val and root.val <= p.val):
                return TreeNode(root.val)
            elif (root.val > p.val and root.val > q.val):
                return self.lowestCommonAncestor(root.left, p, q)
            else:
                return self.lowestCommonAncestor(root.right, p, q)
                

            