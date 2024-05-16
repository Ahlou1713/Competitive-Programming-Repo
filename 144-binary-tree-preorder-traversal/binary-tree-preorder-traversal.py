# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def preOrder(root: TreeNode):
            if root:
                # first add the data of node
                ans.append(root.val)
                # then recur on left child
                preOrder(root.left)
                # finally recur on right child
                preOrder(root.right)
        preOrder(root)
        return ans            
