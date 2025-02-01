class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if s == t: return s
        s = list(s)
        t = list(t)
        minValue = 100000
        minString = ""

        def existArray(long, short):
            if len(long) < len(short): return False
            for char in short:
                if char in long:
                    long.remove(char)
                else:
                    return False
            return True

        for i in range(len(s)-len(t)+1):
            for j in range(i+len(t)-1, len(s)):
                if existArray(s[i:j+1], t):
                    if minValue > j-i+1:
                        minValue = j-i+1
                        minString = "".join(s[i:j+1])
        
        return minString

sol = Solution()

print(sol.minWindow(s = "a", t = "aa"))