class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(magazine) < len(ransomNote): return False

        magDict = {}

        for c in magazine:
            if c in magDict:
                magDict[c] += 1
            else:
                magDict[c] = 1
        

        for c in ransomNote:
            if c in magDict:
                magDict[c] -= 1
                if magDict[c] == 0: del magDict[c]
            else:
                return False
        
        return True
