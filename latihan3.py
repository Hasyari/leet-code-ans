class Solution(object):
    roman_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = self.roman_map[s[-1]]
        for i in range(len(s) - 2, -1, -1):
            if self.roman_map[s[i]] >= self.roman_map[s[i + 1]]:
                result += self.roman_map[s[i]]
            else:
                result -= self.roman_map[s[i]]
        return result


solution = Solution()

print(solution.romanToInt("MCMXCIV"))