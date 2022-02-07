'''
Created on Feb 6, 2022

1. 唉，暴力解法，超时

@author: mayijie
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        res = []

        for curr in enumerate(list(s)):

            # Step 1: handle the odd number: "ccbbabb"
            (i, c, j, tempOdd) = (curr[0], curr[1], 1, [curr[1]])
            while i - j >= 0 and i + j < len(s):
                if list(s)[i-j] == list(s)[i+j]:
                    tempOdd.insert(0, list(s)[i-j])
                    tempOdd.append(list(s)[i+j])
                else:
                    break
                j += 1
            if len(tempOdd) > len(res): res = tempOdd[:]

            # Step 2: handle the even number: "ccbbaabb"
            (i, c, j, tempEven) = (curr[0], curr[1], 0, [])
            while i - j >= 0 and i + j < len(s)-1:
                if list(s)[i-j] == list(s)[i+j+1]:
                    tempEven.insert(0, list(s)[i-j])
                    tempEven.append(list(s)[i+j+1])
                else:
                    break
                j += 1
            if len(tempEven) > len(res): res = tempEven[:]

        return "".join(res)

if __name__ == "__main__":
    sol = Solution()
    res = sol.longestPalindrome("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    print (res)