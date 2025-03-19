'''
1. 递归构造括号字符串，使用 left 记录左括号 ( 的数量，right 记录右括号 ) 的数量。
2. 只有当 left < n 时，才能继续添加 (，以保证左括号不会超过 n。
3. 只有当 right < left 时，才能继续添加 )，以保证右括号不会超前匹配左括号。
4. 当 left == right == n，表示生成了一个完整的有效括号组合，将其加入结果集。
5. 通过回溯返回上一层，尝试新的组合。
'''

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        def dfs(s, left, right):
            if left == n and right == n:
                res.append(s)
                return
            if left < n: dfs(s+'(', left+1, right)
            if right < left: dfs(s+')', left, right+1)
        dfs("", 0, 0)
        return res

sol = Solution()


print(sol.generateParenthesis(3))