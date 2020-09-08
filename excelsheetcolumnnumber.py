class Solution:
    def titletonumber(self, s):
        """
        :type s:str
        """
        total_value = 0
        
        CHARACTER = 26
        ASCII_COMPENSATION = 64
        
        for idx, ch in enumerate(reversed(s)):
            total_value += (CHARACTER ** idx) * (ord(ch) - ASCII_COMPENSATION) 
        
        return total_value
        

print (Solution().titletonumber('AAB'))