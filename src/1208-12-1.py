'''
Created on Dec 8, 2021

1. 两个列表合成一个，时间换空间（注意其中的整数需要从大到小排序）
2. 表示对应关系的dict{}可以使用tuple()来代替，tuple()是有序的，所以可以
   for value, symble in self.role:
   来取tuple中的数据，相比dict，简介异常啊！

@author: mayijie
'''

class Solution:

    role = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

    def single(self, num: int) -> str:
        res = ""
        while num != 0: 
            for value, symble in self.role:
                if num >= value:
                    res += symble
                    num -= value
                    break
        return res

    def intToRoman(self, num: int) -> str:
        i000 = int(num/1000)*1000
        j000 = num%1000
        i00 = int(j000/100)*100
        j00 = j000%100
        i0 = int(j00/10)*10
        j0 = j00%10
        # 分别列出千、百、十、个位
        print (i000, i00, i0, j0)
        return self.single(i000) + self.single(i00) + self.single(i0) + self.single(j0)


if __name__ == "__main__":
    sol = Solution()
    res = sol.intToRoman(1994)
    print (res)