# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        # Case 1: both nodes are None → identical so far
        if not p and not q:
            return True
        
        # Case 2: one of them is None → different structure
        if not p or not q:
            return False

        # Case 3: values differ → not the same
        if p.val != q.val:
            return False

        # Case 4: compare left and right subtrees recursively
        return (self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right))