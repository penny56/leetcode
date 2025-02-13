class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}

        for str in strs:
            temp = tuple(sorted(str))   # 这里不需要用set()，也没必要用set()
            if temp in dic.keys():
                # 已经有同一组的了
                dic[temp].append(str)
            else:
                # 需要新创建
                dic[temp] = [str]

        return list(dic.values())

sol = Solution()


print(sol.groupAnagrams(strs = ["eat", "tea", "tan", "ate", "nat", "bat"]))