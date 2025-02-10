class Solution(object):

    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        def startFrom49(var):
            while var > 10:
                var = var//10
            if var == 4:
                return 4
            elif var == 9:
                return 9
            else:
                return 0
            return False

        dic = {1000: 'M', 500: 'D', 100: 'C', 50: 'L', 10: 'X', 5: 'V', 1: 'I'}
        dicDescArr = [1000, 500, 100, 50, 10, 5, 1]
        flag = 1
        (numArr, resArr) = ([], [])
        while num != 0:
            shift = (num % 10) * flag
            numArr.append(shift)
            num = num // 10
            flag = flag*10
        

        while numArr:
            curr = numArr.pop()
            if curr == 0:
                continue
            elif startFrom49(curr) == 4:
                # use subtraction
                for i in range(len(dicDescArr)):
                    if curr >= dicDescArr[i]:
                        resArr.append(dic[dicDescArr[i]])
                        resArr.append(dic[dicDescArr[i-1]])
                        break
            elif startFrom49(curr) == 9:
                # use subtraction
                for i in range(len(dicDescArr)):
                    if curr >= dicDescArr[i]:
                        resArr.append(dic[dicDescArr[i+1]])
                        resArr.append(dic[dicDescArr[i-1]])
                        break
            else:
                # use addition
                for i in range(len(dicDescArr)):
                    while curr >= dicDescArr[i]:
                        resArr.append(dic[dicDescArr[i]])
                        curr -= dicDescArr[i]
                    # just leave after get the correct stage
                    if curr == 0: break
                    continue

        return resArr    

sol = Solution()


print(sol.intToRoman(3749))