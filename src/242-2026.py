class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        # put s in sDict, the value is the count of characters
        sDict = {}
        for sc in s:
            if sc in sDict:
                sDict[sc] += 1
            else:
                sDict[sc] = 1
        
        for tc in t:
            if tc in sDict:
                if sDict[tc] == 1:
                    del sDict[tc]
                else:
                    sDict[tc] -= 1
            else:
                return False
        
        return True
