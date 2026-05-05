# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        last_level = 0

        q = deque()
        q.append([root, 1])
        right_view = []

        while q:
            node, level = q.popleft()
            if level > last_level:
                right_view.append(node.val)
                last_level = level

            if node.right:
                q.append([node.right, level+1])
            if node.left:
                q.append([node.left, level+1])

        return right_view



