import copy
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(s)<len(p): return []
        res = []

        pDict = dict()
        for value in p:
            if value in pDict.keys():
                pDict[value] += 1
            else:
                pDict[value] = 1

        for i in range(len(s)):
            if i+len(p) <= len(s):
                winArr = list(s[i:i+len(p)])
                currDict = copy.deepcopy(pDict)
                for c in winArr:
                    if c in currDict.keys():
                        currDict[c] -= 1
                        if currDict[c] == 0:
                            del currDict[c]
                    else:
                        # 如果窗口中有一个item不在pDict中，就没必要在当前窗口中花时间了
                        break
                
                if len(currDict) == 0: res.append(i)

        return res

if __name__ == "__main__":
    sol = Solution()
    res = sol.findAnagrams("abab", "ab")
    print(res)