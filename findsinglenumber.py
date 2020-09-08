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




li = [2, 5, 2, 4, 3, 4, 3]
#  010
#^ 001
#^ 010
#= 001 <- Result - Duplicate will have zeros because of even rule here 

print (Solution().find_single_number_2(li))