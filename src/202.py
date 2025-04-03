class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        arr = []

        def helper(n):
            if n == 1: return True
            if n in arr:
                return False
            else:
                arr.append(n)
            
            numsStr = str(n)
            numsSum = 0
            for numChar in numsStr:
                numsSum += int(numChar)*int(numChar)
            return helper(numsSum)

        return helper(n)

if __name__ == "__main__":

    sol = Solution()
    res = sol.isHappy(1)
    print (f"res = {res}")
