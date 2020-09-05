class Solution:
    def threeSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        

        lookup = dict()

        for idx, num in list(enumerate(nums))[:-1]:
            
            # Remaining sum makes it look like we're now working on a two sum problem.
            remainingsum = target - num

            # This is a two sum loop.
            for idx2, num2 in list(enumerate(nums))[idx + 1:]:
            
                if (remainingsum - num2) in lookup:
                    return [idx, idx2, lookup[remainingsum - num2]]
            
                else:
                    lookup[num2] = idx2



solution = Solution()

# Output is the indices of the numbers which sum up.
print ("Indexes : ", solution.threeSum([1, 5, 3, 6, 2], 10))


