class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        axis = 0
        huiwen = s[0]

        # 奇数回文
        for i, axis in enumerate(s):
            for j in range(len(s)//2+1):
                if i-j>=0 and i+j<len(s):
                    if s[i-j] == s[i+j]:
                        if len(huiwen) < j*2+1:
                            huiwen = s[i-j:i+j+1]
                    else:
                        break

        # 偶数回文
        for i, axis in enumerate(s):
            if i+1 < len(s) and s[i] == s[i+1]:
                for j in range(len(s)//2+1):
                    if i-j>=0 and i+j+1<len(s):
                        if s[i-j] == s[i+j+1]:
                            if len(huiwen) < j*2+2:
                                huiwen = s[i-j:i+j+2]
                        else:
                            break
                
        return huiwen

s = "aacabdkacaa"

sol = Solution()

res = sol.longestPalindrome(s)
print ("res = ", res)