# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: return True
        if not p or not q: return False
        if p.val != q.val: return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: return True
        q = deque()
        q.append(root)

        while q:
            node = q.popleft()

            if node.val == subRoot.val:
                is_same = self.isSameTree(node, subRoot)
                if is_same: return True
            
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        return False