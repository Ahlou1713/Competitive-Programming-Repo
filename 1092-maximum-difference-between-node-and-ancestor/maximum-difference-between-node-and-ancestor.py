# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_difference = 0

    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.findMaxAncestorDifference(root, root.val, root.val)
        return self.max_difference

    def findMaxAncestorDifference(self, currentNode, minValue, maxValue):
        if currentNode:
            minValue = min(minValue, currentNode.val)
            maxValue = max(maxValue, currentNode.val)
            self.max_difference = max(self.max_difference, maxValue - minValue)

            self.findMaxAncestorDifference(currentNode.left, minValue, maxValue)
            self.findMaxAncestorDifference(currentNode.right, minValue, maxValue)

