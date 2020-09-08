class Solution:
    
    def find_single_number(self, nums):
        """
        :type nums:List[int]
        :rtype: int
        """
        return 2 * sum(set(nums)) - sum(nums)


    def find_single_number_2(self, nums):
        """
        :type nums:List[int]
        :rtype: int
        """
        ans = 0
        
        for num in nums:
            ans ^= num
        
        return ans




li = [2, 1, 2]

print (Solution().find_single_number_2(li))

