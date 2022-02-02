from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        cp = ''
        i = 0
        while True:
            if len(strs[0]) > i:
                cp += strs[0][i]
                i += 1
                for str in strs:
                    if str.find(cp) != 0:
                        return (cp[:-1])
            else:
                return cp
        
print(Solution().longestCommonPrefix(['flower', 'flow']))