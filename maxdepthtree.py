
class TreeNode:
    
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None



class Solution:

    def maxDepth(self, root):

        if root is None:
            return 0
        
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1



rootp = TreeNode(2)
childpleft = TreeNode(3)
childpright = TreeNode(4)

rootp.left = childpleft
rootp.right = childpright

childpleft.left = TreeNode(4)


print (Solution().maxDepth(rootp))