'''
Created on Dec 8, 2021

1. dict.keys()返回的值不是list，而是dict_keys类型，如果需要list类型，需要转换：firstKey = list(dict.keys())[0]
2. dict与set的区别：
   这两个类型在定义的初始化的时候很像，都是大括号{}，注意一个是带冒号，一个只有逗号：
   -- dict：d = {'name':'tarena', 'age':'15', gender: 'female'}
   -- set： s = {1, 2, 3}

@author: mayijie
'''

class Solution:

    special = {
        4: 'IV', 9: 'IX', 40: 'XL', 90: 'XC', 400: 'CD', 900: 'CM'
    }
    normal = [
        {1000: 'M'}, {500: 'D'}, {100: 'C'}, {50: 'L'}, {10: 'X'}, {5: 'V'}, {1: 'I'}
    ]
    def single(self, num: int) -> str:
        if num == 0:
            return ""
        if num in self.special:
            return self.special[num]
        res = ""
        while num != 0:
            for pair in self.normal:
                if num >= list(pair.keys())[0]:
                    res += list(pair.values())[0]
                    num -= list(pair.keys())[0]
                    # 这里需要跳到for循环外，因为normal里的每一个字典可能需要用多次
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