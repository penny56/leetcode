class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        # place the characters in magazion into a dict
        mDict = {}

        for mc in magazine:
            if mc in mDict:
                mDict[mc] += 1
            else:
                mDict[mc] = 1
        
        for rc in ransomNote:
            if rc not in mDict:
                return False
            else:
                if mDict[rc] == 1:
                    del mDict[rc]
                else:
                    mDict[rc] -= 1
        
        return True
