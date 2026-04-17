class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        minAltitude = -float('inf')
        altList = [0]
        curr = 0
        for g in gain:
            curr = curr + g
            altList.append(curr)
        print(f'altList = {altList}')
        return max(altList)

