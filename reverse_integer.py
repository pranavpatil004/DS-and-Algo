class Solution:
    def reverse(self, x: int) -> int:
        abs_number= abs(x)
        final_number = 0
        while abs_number > 0:
            remainder = abs_number%10
            final_number = final_number *10 + remainder
            abs_number = abs_number/10
        if final_number >= (2**31):
            return 0
        return final_number if x > 0 else final_number*-1

Solution().reverse(123)