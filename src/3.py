class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        array = list(s)
        max = 0
        if len(s) == 1: return 1

        for i, a in enumerate(array):
            for j, c in enumerate(array):
                if i < j:
                    print (f"{i} {j}")
                    sub = array[i:j+1]
                    print (f"sub = {sub}")
                    unique = set(sub)
                    print (f"unique = {unique}")
                    if (len(unique) == 1 or len(sub) == len(unique)) and len(unique) > max:
                        max = len(unique)
                        print (f"max = {max}")

        return max

s = "abcabcbb"

sol = Solution()

res = sol.lengthOfLongestSubstring(s)
print ("res = ", res)