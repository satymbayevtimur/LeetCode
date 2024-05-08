# Reverse entire number

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        reversedNumber = 0
        temporary = x

        while temporary != 0:
            digit = temporary % 10
            reversedNumber = reversedNumber * 10 + digit
            temporary //= 10

        return reversedNumber == x

# Reverse half of the number

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        
        reversedNumber = 0
        originalNumber = x

        while x > reversedNumber:
            reversedNumber = reversedNumber * 10 + x % 10
            x //= 10

        return x == reversedNumber or x == reversedNumber // 10
