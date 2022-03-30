# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Could we pass some x values down and just collate all the values which pop up at those x values
        # Don't Froget about your edge cases
        if root == None:
            return None
        vertical_order = defaultdict(lambda:[])
        # def _dfs(root, x=0):
        #     vertical_order[x].append(root.val)
        #     if root.left:
        #         _dfs(root.left, x-1)
        #     if root.right:
        #         _dfs(root.right, x+1)
        # _dfs(root)
        # Did not seem to work.
        # let's try BFS
        queue = deque()
        queue.append([root, 0])
        while queue:
            root, x = queue.popleft()
            vertical_order[x].append(root.val)
            if root.left:
                queue.append([root.left, x-1])
            if root.right:
                queue.append([root.right, x+1])
        order = list(vertical_order.keys())
        order.sort()
        return [vertical_order[v] for v in order]
        