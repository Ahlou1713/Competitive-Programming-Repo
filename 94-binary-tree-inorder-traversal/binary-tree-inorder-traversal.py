# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def inOrder(root: TreeNode):
            if root:
                # first recur on left child
                inOrder(root.left)
                # then add the data of node
                ans.append(root.val),
                # now recur on right child
                inOrder(root.right)
        inOrder(root)
        return ans