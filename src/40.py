'''
全局变量：
candidates[]: 
res[]:

递归参数：
path[]: 当前branch已走过的路径
target: 当前递归要找到的目标数

终止条件：
1. target < 0: 返回
2. target == 0: path入栈


递推工作：
1. 遍历candidates[]，如果< target的，就递归


返回值：
None

'''


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []

        def dfs(path, candidates, target):
            if target == 0:
                res.append(path[:])
                return
            for i, candidate in enumerate(candidates):
                if candidate <= target:
                    path.append(candidate)
                    dfs(path, candidates[:i]+candidates[i+1:], target-candidate)
                    path.pop()
        
        dfs(path=[], candidates=candidates, target=target)

        # 消除重复
        s = set()
        for r in res:
            s.add(tuple(sorted(r)))
        res.clear()
        for uni in s:
            res.append(list(uni))

        return res
            


sol = Solution()


print(sol.combinationSum(candidates = [2,5,2,1,2], target = 5))