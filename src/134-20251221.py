from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        if n == 1: return 0
        flag = False
        for start in range(n):
            tank = 0
            stop_num = 0
            station_num = 0
            while stop_num < n:
                station_num = (start + stop_num) % n
                tank += gas[station_num]
                tank -= cost[station_num]
                if tank < 0: break
                stop_num += 1
            
            if stop_num == n: flag = True

            if flag: return start
        
        return -1
    
sol = Solution()

res = sol.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2])

print(res)

