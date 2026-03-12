class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazionList = list(magazine)
        for c in ransomNote:
            if c in magazionList:
                magazionList.remove(c)
            else:
                return False
        return True
