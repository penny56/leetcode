import re

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0: return strs.pop(0)
        
        shortest_str = min(strs, key=len)

        strs.remove(shortest_str)
        matched = 0
        
        while len(shortest_str) > 0:
            matched = 0
            for str in strs:
                if re.match(shortest_str, str) != None: matched += 1
                if matched == len(strs): return shortest_str
            shortest_str = shortest_str[:-1]

        return ""




sol = Solution()

res = sol.longestCommonPrefix(["a"])
print ("res = ", res)