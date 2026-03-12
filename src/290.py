class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d = {}
        sList = s.split()

        if len(pattern) != len(sList): return False

        for i in range(len(pattern)):
            if pattern[i] not in d:
                # judge if value already in values set
                if sList[i] in d.values(): return False
                # add the key/value pair into dict
                d[pattern[i]] = sList[i]

                
            else:
                # this pattern already in the dict
                if d[pattern[i]] != sList[i]: return False

        return True
