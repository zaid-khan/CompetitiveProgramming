import sys

class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype List[int]
        """

        nums.sort()
        minimum = sys.maxsize
        answer = []

        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums)-1

            while (j < k):
                total = nums[i] + nums[j] + nums[k]

                diff = target - total 
                if (diff == 0):
                    return [nums[i], nums[j], nums[k]]
                
                elif (diff < 0):
                    k -= 1
                
                else:
                    j += 1

                if (abs(diff) < minimum):
                    minimum = diff
                    answer = [nums[i], nums[j], nums[k]]
        
        return answer

print(Solution().threeSumClosest(nums=[1,5,3,6,2], target=6))