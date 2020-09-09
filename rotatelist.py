class Solution:
    
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void
        """

        n = len(nums)

        if (n == 1 or k == 0 or n == k):
            return

        k = k % n

        g_c_d = self.gcd(n, k)

        for idx in range(g_c_d):
            jdx = idx
                
            prev = nums[jdx]    
            
            while True:  
                # kdx points to the element under consideration
                kdx = (jdx + k) % n

                # Swapping the previous element with the current element
                prev, nums[kdx] = nums[kdx], prev

                jdx = kdx 

                if jdx == idx:
                    break
    

    def gcd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        if (m % n == 0):
            return n
        else:
            return self.gcd(n, m % n)

    
    def rotate2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void
        """

        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]

    
    def rotate_like_gcd_but_better(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void
        """
        n = len(nums)
        k %= n
        
        start = count = 0
        while count < n:
            current, prev = start, nums[start]
            while True:
                next_idx = (current + k) % n
                nums[next_idx], prev = prev, nums[next_idx]
                current = next_idx
                count += 1
                
                if start == current:
                    break
            start += 1

nums = [1, 2, 3, 4, 5, 6, 7]
Solution().rotate(nums, 3)
print (nums)