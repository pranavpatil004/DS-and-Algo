import time
start_time = time.time()
class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C':  100, 'D': 500, 'M': 1000}
        final_number = 0
        prev_char = ''
        print(" 1 --- %s seconds ---" % (time.time() - start_time))
        for char in s:
            final_number += mapping[char]
            if (char in ['V', 'X'] and prev_char == 'I') or (char in ['L', 'C'] and prev_char == 'X') or (char in ['D', 'M'] and prev_char == 'C'):
                final_number -= 2 * mapping[prev_char]
            prev_char = char
            print(" for --- %s seconds ---" % (time.time() - start_time))
        return final_number

print(Solution().romanToInt('MCMXCIV'))
print("--- end %s seconds ---" % (time.time() - start_time))