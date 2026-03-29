from typing import List
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def verticalTraversal(self,root: Optional[TreeNode]) -> List[List[int]]:
        nodes=[]
        #记录每个节点的（行，列）
        def dfs(node, row, col):
            if not node:
                return
            nodes.append((col, row, node.val)) #先按col，col相同再按row,row相同再按val
            dfs(node.left,row+1,col-1)
            dfs(node.right, row+1,col+1)
        
        dfs(root,0,0)

        #排序准备提取node
        nodes.sort()
        res=[]
        #每次新建一个col组团的前提是换col了
        prev=float('inf')
        for c, r, val in nodes:
            if c!=prev:
                res.append([])
                prev=c
            res[-1].append(val)
        return res