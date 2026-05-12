class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) == 2: return min(height[0], height[1])

        (i, j) = (0, len(height)-1)
        maxValue = 0

        while i != j:
            current = (j-i) * min(height[i], height[j])

            if current > maxValue: maxValue = current

            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
        
        return maxValue
