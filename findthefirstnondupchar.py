class Solution:
    def firstcharacterwhichisunique(self, text):
        """
        :type text: str
        :rtype: char
        """
        lookup = dict()
        for char in text:
            if char in lookup:
                lookup[char] = lookup[char] + 1
            else:
                lookup[char] = 1
        
        for char in text:
            if (lookup[char] == 1):
                return char

        return None


print(Solution().firstcharacterwhichisunique('leelttccoodde'))

