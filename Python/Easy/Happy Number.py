class Solution:
    def isHappy(self, n: int) -> bool:
        def new_digit(n, seen):
            n = str(n)
            a = 0
            for i in n:
                a += (int(i)) ** 2
            if a == 1:
                return True   
            if a in seen:
                return False

            seen.add(a)
            
            flag = new_digit(a, seen)
            return flag

        return new_digit(n, set())
