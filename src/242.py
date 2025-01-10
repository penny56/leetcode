class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ss = list(s).sort()
        print(f"ss = {ss}")
        tt = sorted(list(s))
        print(f"tt = {tt}")
        if ss == tt:
            return True
        else:
            return False


sol = Solution()

s = "anagram"
t = "nagaram"

sol.isAnagram(s, t)
