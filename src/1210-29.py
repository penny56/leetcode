'''
Created on Dec 10, 2021

1. 表示乘方用**：如4的5次方 = 4*4*4*4*4 = 4**5 = 1024
2. 不对超时！

@author: mayijie
'''


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        # 处理特殊情况
        if divisor == 0: return 0
        if divisor == -2*31:
            return 1 if dividend == -2**31 else 0
        if divisor == 1: return dividend
        if divisor == -1 and dividend != -2**31: return 0-dividend
        if dividend == -2**31:
            if divisor == 1: return -2**31
            if divisor == -1: return 2**31-1
        
        # 找出正负数
        positive = True
        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0): positive = False

        # 处理一般情况
        (times, sum) = (0, abs(divisor))
        while sum <= abs(dividend):
            times += 1
            sum += abs(divisor)
        return times if positive else 0-times

if __name__ == "__main__":
    sol = Solution()
    res = sol.divide(2147483647,2)
    print (res)