class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.res = 0
        
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            #最长路径长度就是 左子树最大深度 + 右子树最大深度
            self.res = max(self.res, left + right)
            return 1 + max(left, right)
        
        dfs(root)
        return self.res