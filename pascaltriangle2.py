# The genius of the zip method.
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        ans = [1]
        # 'ans' stores the previous answer
        for _ in range(rowIndex):
            ans = [x+y for x, y in zip([0]+ans, ans+[0])]
        return ans

#       1 
#     1  1              1  1  =     0 1 + 1 0
#    1  2  1          1  2  1  =  0 1 1 + 1 1 0
#  1  3   3  1      1  3  3  1  =  0 1 2 1 + 1 2 1 0  

print (Solution().getRow(3))