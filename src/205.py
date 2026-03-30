class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        if len(s) != len(t): return False
        (sTot, tTos) = ({}, {})

        for i in range(len(s)):
            if s[i] in sTot:
                if sTot[s[i]] != t[i]:
                    return False
            else:
                sTot[s[i]] = t[i]

            if t[i] in tTos:
                if tTos[t[i]] != s[i]:
                    return False
            else:
                tTos[t[i]] = s[i]
        
        return True
