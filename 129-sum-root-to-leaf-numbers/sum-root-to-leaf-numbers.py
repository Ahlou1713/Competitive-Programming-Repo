# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        
        global leftSide
        leftSide = []

        def dfs(root, curr):
            if not root:
                pass
            elif not root.left and not root.right:
                curr += str(root.val)
                leftSide.append(curr)
            else:
                curr += str(root.val)
                all_curr = curr[:]
                dfs(root.left, curr)
                dfs(root.right, all_curr)

        dfs(root, '')
        result = 0
        for i in leftSide:
            result += int(i)
        return result