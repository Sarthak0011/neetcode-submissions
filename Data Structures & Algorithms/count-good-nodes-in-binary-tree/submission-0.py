# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root: return 0

        count = 0
        q = deque()
        q.append([root, -101])

        while q:
            node, prev_max = q.popleft()

            if node.val >= prev_max:
                count += 1
            
            if node.left:
                q.append([node.left, max(prev_max, node.val)])
            if node.right:
                q.append([node.right, max(prev_max, node.val)])
        
        return count