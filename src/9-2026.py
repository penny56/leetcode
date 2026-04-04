class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False

        # 转成 str
        xStr = str(x)
        if len(xStr) == 1: return True 

        xStrR = xStr[::-1]

        if xStrR[0] == '0': return False
        for i in range(len(xStr)):
            if xStr[i] != xStrR[i]: return False
        
        return True
