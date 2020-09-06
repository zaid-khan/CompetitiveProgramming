class Solution:
    """
    :type roman: string
    :rtype: int
    """
    def romanToArabic(self, roman):
        
        roman_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500
        }
        
        nums = [roman_to_int[letter] for letter in roman]

        arabic = nums[-1]

        for idx in range(1, len(roman)):

            if (nums[-idx - 1] >= nums[-idx]):
                arabic += nums[-idx - 1]
            else:
                arabic -= nums[-idx - 1] 

        return arabic



print (Solution().romanToArabic('VI'))
