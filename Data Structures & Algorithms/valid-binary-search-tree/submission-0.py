# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfsSolver(root: Optional[TreeNode], left_boundary: int, right_boundary: int) -> bool:
            if not root:
                return True
            
            if not left_boundary < root.val < right_boundary:
                return False

            left_ans = dfsSolver(root.left, left_boundary, root.val)
            right_ans = dfsSolver(root.right, root.val, right_boundary)

            return left_ans and right_ans
        
        return dfsSolver(root, float("-inf"), float("inf"))
