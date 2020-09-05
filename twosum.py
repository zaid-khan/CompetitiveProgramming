class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lookup = {}
        for idx, num in enumerate(nums):
            if target - num in lookup:
                return [lookup[target-num], idx]
            lookup[num] = idx


nums = [1, 5, 2, 8]
target = 7

solution = Solution()
print ("Indexes :", solution.twoSum(nums, target))