class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """

        res = []
        def helper(cnt, arr):
            nonlocal n
            
            if cnt == n:
                res.append(arr)
                return
            rra = arr[::-1]
            for i in range(len(arr)):
                arr[i] = '0'+arr[i]
            for i in range(len(rra)):
                rra[i] = '1'+rra[i]
            
            res.append(arr+rra)

            helper(cnt+1, arr+rra)

        helper(1, ['0', '1'])

        def binary_list_to_decimal(binary_list):
            return [int(binary, 2) for binary in binary_list]

        return binary_list_to_decimal(res.pop())
        

sol = Solution()

res = sol.grayCode(2)

print(f"res = {res}")