# 抄袭ChatGPT！
# 记住: str类型也可以使用下标来表示：s[i]；与list的区别是str中的元素不可改变。

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0: return True
        if len(s) > len(t): return False

        (i, j) = (0, 0)
        while i < len(s):
            while j < len(t) and t[j] != s[i]:
                j += 1
            if j == len(t): return False
            
            i += 1
            j += 1

        return True
