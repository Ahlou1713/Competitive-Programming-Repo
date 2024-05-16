# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def postOrder(root: TreeNode):
            if root:
                # first recur on left child
                postOrder(root.left)
                # then recur on right child
                postOrder(root.right)
                # then add the data of node
                ans.append(root.val)
        postOrder(root)
        return ans