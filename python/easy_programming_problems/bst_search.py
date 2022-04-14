# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root.val == val:
            return root
        else:
            if val < root.val and root.left != None:
                return self.searchBST(root.left, val)
            elif val > root.val and root.right != None:
                return self.searchBST(root.right, val)
            return None