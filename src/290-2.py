class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        sList = s.split()

        if len(pattern) != len(sList): return False

        pDict = {}
        
        for i in range(len(pattern)):
            if pattern[i] in pDict:
                if sList[i] != pDict[pattern[i]]: return False
            else:
                # 如果没有在dict中，先要判断新value有没有在旧values中
                if sList[i] in pDict.values(): return False
                # 之后再加到pDict中
                pDict[pattern[i]] = sList[i]
        
        return True
