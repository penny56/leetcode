class Solution:
    def romanToInt(self, s: str) -> int:

        # 通常：先大后小： XII = = 10+1+1 = 12
        # 特殊：先小后大： IV = 5-1 = 4 | IX = 10 - 1 = 9
        # 特殊情况用于：
        #              IV: 4   | IX: 9
        #              XL: 40  | XC: 90
        #              CD: 400 | CM: 900

        trans1 = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        trans2 = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}

        skip = False
        res = 0

        for i in range(len(s)):
            if skip:
                skip = False
                continue
            else:
                if i < len(s)-1 and s[i]+s[i+1] in trans2:
                    # 先判断是否是特殊情况
                    res += trans2[s[i]+s[i+1]]
                    skip = True
                else:
                    # 一般情况
                    res += trans1[s[i]]
        
        return res
                

