class Solution:
    def find_major_element(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        element = nums[0]
        count = 1
        
        for num in nums[1:]:
        
            if num == element:
                count += 1
            
            else:
                count -= 1
                if count == 0:
                    element = num
                    count = 1
        
        return element


print(Solution().find_major_element([2, 2, 1, 2, 1, 2, 3]))