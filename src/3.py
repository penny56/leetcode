class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        maxLength = 0
        for k in range(len(s)):
            (i, j) = (k, k)
            (istop, jstop) = (False, False)
            while not (istop and jstop):
                if i-1>=0 and s[i-1] not in s[i:j+1]:
                    i -= 1
                else:
                    istop = True
                if j+1 <= len(s)-1 and s[j+1] not in s[i:j+1]:
                    j += 1
                else:
                    jstop = True
            if j-i+1 > maxLength: maxLength = j-i+1
        
        return maxLength

            

sol = Solution()
print(sol.lengthOfLongestSubstring(s = ""))