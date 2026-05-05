# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return None
        q = deque()
        curr = root
        q.append(curr)

        while q:
            node = q.popleft()

            left_node = node.left
            right_node = node.right

            node.right = left_node
            node.left = right_node

            if left_node:
                q.append(left_node)
            if right_node:
                q.append(right_node)

        return root
