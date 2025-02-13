'''
dfs() 递归方法
'''


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        (resSet, res) = (set(), [])

        def dfs(path, candidates):
            if not candidates:
                resSet.add(tuple(path))
                return
            for i, candidate in enumerate(candidates):
                path.append(candidate)
                dfs(path, candidates[:i]+candidates[i+1:])
                path.pop()
        
        dfs(path = [], candidates = nums)

        # 去重
        for rs in resSet:
            res.append(list(rs))
        
        return res

sol = Solution()


print(sol.permute(nums = [1,1,2]))