class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # 不能直接从最小的0，1，2个字串开始。
        # 要从长度小的字串开始。

        # 把res赋值成较短的那个str
        res = str1 if len(str1) <= len(str2) else str2
        resMultiTimes = 0
        while len(res) > 0:
            (str1Flag, str2Flag) = (False, False)

            if len(str1)%len(res) == 0:
                resMultiTimes = len(str1)//len(res)
                resTmp = res * resMultiTimes
                
                if resTmp == str1: str1Flag = True

            
            if len(str2)%len(res) == 0:
                resMultiTimes = len(str2)//len(res)
                resTmp = res * resMultiTimes

                if resTmp == str2: str2Flag = True

            if str1Flag and str2Flag: return res

            res = res[:-1]
        
        return ""
