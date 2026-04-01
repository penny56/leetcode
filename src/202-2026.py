class Solution:
    def isHappy(self, n: int) -> bool:
        # 这个想法就是：不会是无阻不循环，因为3位最大数 999，算出的平方和 81+81+81=243，反而小了。
        # 如果出现某个数，之前出现过，就一定会循环
        # 所以只要记录之前的数，每出现一个新数，判断。
        def intTolist(num: int) -> list:
            res = []
            while num > 0:
                ys = num % 10
                res.append(ys)
                num = num // 10
            
            return res

        s = set()

        while True:
            digitList = intTolist(n)
            sos = 0
            for digit in digitList:
                sos += digit*digit

            if sos == 1: return True

            if sos in s:
                return False
            else:
                s.add(sos)
                n = sos


