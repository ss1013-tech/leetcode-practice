class TreeNode:
    def __init__(self, val:int):
        self.val=val
        self.left=None
        self.right=None

class Codec:
    def serialize(self, root):
        vals = []
        def dfs(node):
            if not node:
                vals.append("N")
                return
            vals.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(vals) #这里要加一个分隔符，不然如果1，2合并在一起不知道是1，2 还是12

    def deserialize(self, data):
        vals = data.split(",")
        self.i = 0
        def dfs():
            if vals[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()