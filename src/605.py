class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        if n == 0: return True
        
        for i, taken in enumerate(flowerbed):
            if i == 0:
                '''
                这里要单独处理，因为在[start: end)中:
                当 start < -1时，比如[-3: ]会截取到0，[0: ]
                当 start == -1时，就出问题了，因为这时 -1 表示 end-1，所以整个 slice 会成为空list
                '''
                bed = flowerbed[:2]
            else:    
                bed = flowerbed[i-1:i+2]

            if 1 not in bed:
                # 种花
                flowerbed[i] = 1
                n -= 1
                if n == 0: return True
        
        return False
