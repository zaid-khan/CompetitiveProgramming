class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isTreeSame(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        
        if (p is None and q is None):
            return True
        
        if (p is None and q is not None) or (p is not None and q is None):
            return False

        if p.val != q.val:
            return False
        
        if self.isTreeSame(p.left, q.left):
            return self.isTreeSame(p.right, q.right)
        
        return False

rootp = TreeNode(2)
childpleft = TreeNode(3)
childpright = TreeNode(4)

rootq = TreeNode(2)
childqleft = TreeNode(3)
childqright = TreeNode(4)

rootp.left = childpleft
rootp.right = childpright

rootq.left = childqleft
rootq.right = childqright


print (Solution().isTreeSame(rootp, rootq))

