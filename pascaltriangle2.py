class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        ans = [1]
        for _ in range(rowIndex):
            ans = [x+y for x, y in zip([0]+ans, ans+[0])]
        return ans

print (Solution().getRow(1))