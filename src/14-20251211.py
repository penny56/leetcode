class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if len(strs) == 1: return strs[0]

        tset = set()
        res = []
        end = False
        while True:
            tset.clear()
            i = 0
            for str in strs:
                if len(str) == 0:
                    return "".join(res)
                else:
                    tset.add(str[0])
                    strs[i] = str[1:]
                    i += 1
            if len(tset) != 1:
                return "".join(res)
            res.append(tset.pop())

        
sol = Solution()

strs = ["dog","racecar","car"]

res = sol.longestCommonPrefix(strs)

print(f"{res}")