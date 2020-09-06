class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    @staticmethod
    def printInOrderTree(root):
        if root is not None:
            TreeNode.printInOrderTree(root.left)
            print (root.val, end=' ')
            TreeNode.printInOrderTree(root.right)
        


class Solution:
    def convertArrayToBST(self, left, right, sortedarray):
        """
        :type sortedarray: List[int]
        :type left: int
        :type right: int
        :rtype TreeNode
        """

        if (left < right):
            mid = (right + left) // 2

            node = TreeNode(sortedarray[mid])
            node.left = self.convertArrayToBST(left, mid, sortedarray)
            node.right = self.convertArrayToBST(mid + 1, right, sortedarray)

            return node
        
        return None


TreeNode.printInOrderTree(Solution().convertArrayToBST(0, 5, [1,2,3,4,5]))