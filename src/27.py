class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # 2 indexes: left and right, left start for 0 and move to the right, right start from len(nums)-1 and move to the left
        # till left == right

        if not nums: return 0
        if len(nums) == 1:
            if nums[0] == val:
                nums.pop()
                return 0
            else:
                return 1
        
        (left, right) = (0, len(nums)-1)
        while left <= right:
            if nums[left] == val:
                # 这里只需要判断left == val
                # 无需判断 right == val
                # 因为在互换之后，right 会左移，而left在下一个loop还会判断，总体是驱中的
                (nums[left], nums[right]) = (nums[right], nums[left])
                right -= 1
            else:
                left += 1
        return left
