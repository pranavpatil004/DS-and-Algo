class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        xi,xj = x, x
        i = 1
        j = len(str(x))-1
        while i<=j:
            xi, remi = divmod(xi, 10)
            remj = int(xj/10**j)
            xj -= remj*(10**j)
            if remi != remj:
                return False
            i += 1
            j -= 1
        return True

print(Solution().isPalindrome(-10))