class Solution:
    def reverseWords(self, s: str) -> str:
        sList = s.split()

        # no need to reverse, because the pop() method start from the last
        # sList.reverse()

        res = ""
        while(sList):
            res += sList.pop()
            res += ' '
        
        # remove the last blank
        return res[:-1]
