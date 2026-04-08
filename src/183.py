class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 把所有非0的元素，按顺序放入arr
        arr = []
        for num in nums:
            if num != 0: arr.append(num)

        for i in range(len(nums)):
            if i < len(arr):
                # len(arr) 及之前的元素，放回nums
                # nums[i] = arr[i]
                nums[i] = arr.pop(0)
            else:
                # 之后的元素，填充0
                nums[i] = 0

        return
