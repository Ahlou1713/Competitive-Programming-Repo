# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        arr = []
        def inOrder(root: TreeNode):
            if root:
                # first recur on left child
                inOrder(root.left)
                # then add the data of node
                arr.append(root.val),
                # now recur on right child
                inOrder(root.right)
        inOrder(root)


        def buildBalancedBST(start, end) -> TreeNode:
            if start > end:
                return None
            mid = start + (end-start) // 2
            node = TreeNode(arr[mid])
            node.left = buildBalancedBST(start, mid - 1)
            node.right = buildBalancedBST(mid + 1, end)
            return node
        
        return buildBalancedBST(0, len(arr) - 1)