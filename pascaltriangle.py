class Solution(object):

    def generatePascalTri(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        triangle = list(list())
        
        for r in range(0, numRows):
            
            # Intelligent use of expanding a list (vector) using a number (scalar).
            row = [1] * (r + 1)
        
            for c in range(1, r):  
                # Present state dependent upon old state.
                row[c] = triangle[r - 1][c - 1] + triangle[r - 1][c]

            # Present state gets appended to old state.
            triangle.append(row)
        
        return triangle


solution = Solution()
print (solution.generatePascalTri(5))
