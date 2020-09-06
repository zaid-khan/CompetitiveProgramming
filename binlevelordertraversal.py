class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
class Solution2:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def dfs(node, depth):
            if node is None:
                return
            if len(self.ans) > depth:
                self.ans[-1-depth].append(node.val)
            else:
                self.ans = [[node.val]]+self.ans
            dfs(node.left, depth+1)
            dfs(node.right, depth+1)
        
        self.ans = []
        dfs(root, 0)
        return self.ans


class Solution:
    def bfs(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        traversedvalues = list()
        queue = list()
        queue.append(root)

        while (queue):
            currentnode = queue.pop(0)
            
            if (currentnode.left):
                queue.append(currentnode.left)
            
            if (currentnode.right):
                queue.append(currentnode.right)
            
            traversedvalues.append(currentnode.val)
        
        return traversedvalues

    def dfs(self, node, depth):

        if node is None:
            return
        
        if len(self.leveltraversed) > depth:
            self.leveltraversed[-depth - 1].append(node.val)
        else:
            self.leveltraversed = [[node.val]] + self.leveltraversed
        
        self.dfs(node.left, depth + 1)
        self.dfs(node.right, depth + 1)


    def levelOrderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        self.leveltraversed = []
        self.dfs(root, 0)
        return self.leveltraversed
        
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(8)
root.left.right.left = TreeNode(9)
root.left.right.right = TreeNode(10)
root.right.right.left = TreeNode(11)

print (Solution().levelOrderTraversal(root))