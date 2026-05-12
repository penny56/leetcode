class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        (res, d) = ([], {})
        
        for str in strs:
            # 1 生成一个tuple，是str的所有字母排序
            strTuple = tuple(sorted(str))

            # 2 以 strTuple 为 key，以str[]为value.先判断这个key是否已存在
            if strTuple in d:
                # 3 如果存在，就加入value list
                d[strTuple].append(str)
            else:
                # 4 如果不存在，创建一个 key/value 对，并把当前str放入value
                d[strTuple] = [str]

        for v in d.values():
            res.append(v)

        return res
