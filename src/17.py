class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dic = {'2':('a','b','c'), '3':('d','e','f'), '4':('g','h','i'), '5':('j','k','l'), '6':('m','n','o'), '7':('p','q','r','s'), '8':('t','u','v'), '9':('w','x','y','z')}
        
        digits = str(digits)
        if digits == "": return []
        res = list(dic[str(digits)[0]])
        digits = digits[1:]
        for num in digits:
            # loop1, 依次处理数字，如按了246，依次处理246
            tails = dic[num]
            resTemp = []
            while len(res) > 0:
                # loop2，依次处理res，如res=[a,b,c]
                for tail in tails:
                    # loop3, 依次让 res 里的元素与 tails 里的元素组合。
                    resTemp.append(res[0]+tail)
                res.pop(0)
            res = resTemp[:]

        return res
            

sol = Solution()


print(sol.letterCombinations(234))