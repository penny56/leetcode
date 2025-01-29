class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        res = []
        wordLen = len(words[0])
        wordCnt = len(words)
        subStringLen = wordLen*wordCnt

        if len(s) < subStringLen: return []

        for i in range(len(s)-subStringLen+1):
            print(f"i={i}")
            duplwords = words[:]
            currWords = []
            for j in range(i, i+subStringLen, wordLen):
                print(f"  j={j}")
                currWords.append(s[j:j+wordLen])
            print(f"  currWords={currWords}")
            
            if len(duplwords) == len(currWords):
                cnt = 0
                while cnt < len(words):
                    temp = duplwords.pop()
                    if temp in currWords:
                        currWords.remove(temp)
                    else:
                        break
                    cnt += 1
                if not currWords: res.append(i)
        
        return res

sol = Solution()


print(sol.findSubstring("barfoothefoobarman", ["foo","bar"]))