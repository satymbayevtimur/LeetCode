# First approach

class Solution:
    def romanToInt(self, s: str) -> int:
        numbers = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        result = 0

        for i in range(len(s)):
            if i < len(s) - 1 and numbers[s[i]] < numbers[s[i + 1]]:
                result -= numbers[s[i]]
            else:
                result += numbers[s[i]]

        return result

# Second approach

class Solution:
    def romanToInt(self, s: str) -> int:
        numbers = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        result = 0

        s = s.replace('IV', 'IIII').replace('IX', 'VIIII').replace('XL', 'XXXX').replace('XC', 'LXXXX').replace('CD', 'CCCC').replace('CM', 'DCCCC')

        for character in s:
            result += numbers[character]

        return result
