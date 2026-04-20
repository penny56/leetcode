class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arrSet = set(arr)
        diffNumCnt = len(arrSet)
        
        unique = {}

        for num in arr:
            if num in unique:
                unique[num] += 1
            else:
                unique[num] = 1
        
        if len(arrSet) == len(set(unique.values())):
            return True
        else:
            return False
