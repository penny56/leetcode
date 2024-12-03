class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        tList = s.split(' ')
        notNone = []
        for str in tList:
            if str != "":
                notNone.append(str)
        last = notNone[-1]
        res = len(last)


        return res


sol = Solution()

res = sol.lengthOfLastWord("   fly me   to   the moon  ")
print ("res = ", res)





