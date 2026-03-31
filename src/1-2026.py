class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDict = {}
        
        # 1 put elements in list to dict, the keys are indexes, the values are elements
        for i, num in enumerate(nums):
            numsDict[i] = num

        # 2 go throught the list, if the delta in the values in the dict, return the index of list and the key of the dict value
        for iList, numList in enumerate(nums):
            delta = target - numList

            if delta in numsDict.values():
                for iDict, numDict in numsDict.items():
                    if numDict == delta and iDict != iList: return [iList, iDict]
