'''
Created on Dec 8, 2021

1. typing是定义List的package
2. nums.sort() -> Yes
   nums = nums.sort() -> No!
3. 先不排序，用 threeSum-k=twoSum，再在剩余的数里找最接近和为 twoSum 的 pair
4. range()的用法：
   - syntax：range([start,] stop [, step]) -> range object
   - 输入：start (optional): 起始数，默认=0
          stop (required): 停止数
          step (optional): 步长，默认=1
   - 输出：在Py3里，输入是range object，在Py2里，输出是list，但是在Py3里，也可以用 for i in output: 去遍历；也可以用list(range(5))把输出转成list类型
   - 注意：range()的输入只能是起始、结束和步长的数字；输出只能是一个数字列表哦。
5. for循环怎么拿到每个元素的index？
   - 可以用  for idx, vlu in enumerate(array)
6. 蠢办法，超时！

@author: mayijie
'''

from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        min = 10000
        for i, vi in enumerate(nums):
            for j, vj in enumerate(nums):
                if j <= i:
                    continue
                for k, vk in enumerate(nums):
                    if k <= j:
                        continue
                    # print (i, j, k)
                    if abs(vi+vj+vk-target) < min:
                        min = abs(vi+vj+vk-target)
                        (ii, jj, kk) = (vi, vj, vk)
                        res = vi+vj+vk
        # print ("last set: ", ii, jj, kk)
        return res


if __name__ == "__main__":
    sol = Solution()
    res = sol.threeSumClosest([47,-48,-72,97,-78,50,-22,18,9,24,28,-53,44,-96,50,45,86,11,21,-44,67,83,55,-86,-33,0,-53,-94,-60,57,-72,-73,-27,13,91,80,18,-80,-29,-69,-74,-90,54,22,3,91,-47,-32,80,-55,69,-95,62,-92,4,-86,62,3,23,-30,-4,0,49,24,10,-32,79,-99,-66,-30,-83,-13,90,-27,9,-4,9,98,-70,-19,32,24,-77,83,11,-78,-94,4,41,61,20,96,-36,54,-46,-51,91,54,30,-42,82,0,9,24,-2,32,-16,-18,87,23,78,-10,-82,-67,68,-18,-61,91,-90,-53,67,-48,12,1,-71,-99,31,82,39,-56,23,-89,-58,19,-60,39,-23,-76,-85,67,-33,69,-74,-8,-99,52,-70,-71,85,-8,28,-3,-100,18,88,5,-16,17,91,-35,22,-76], 298)
    print (res)