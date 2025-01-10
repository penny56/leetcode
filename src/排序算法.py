class Solution(object):
    '''
    冒泡排序每次比较相邻的两个元素，如果顺序不对就交换它们。
    每一轮j遍历后，当前最大的元素会被移动到列表的末尾。
    是“泡泡”到列表头，还是“石头”到列表尾，是看j遍历在头结束，还是尾结束。
    如果是从左到右循环，肯定是尾结束，是“沉底”
    '''
    def bubbleSort(self, arr):
        for i in range(len(arr)):                               #1. i: 0 -> len()
            for j in range(len(arr)-i-1):                       #2. j: 0 -> len()-i-1   沉底（还要保证 j+1 不越界）
                if arr[j] > arr[j+1]:                           #3. a[j] > a[j+1]  如果左边的大：
                    (arr[j], arr[j+1]) = (arr[j+1], arr[j])     #4. 交换

        return arr
    
    '''
    递归算法
    '''
    def quickSort(self, arr):
        if len(arr) <= 1: return arr

        pivot = arr[0]                          #1. 取 arr[0] 为 pivot

        (less, greater) = ([], [])              #2. 定义 less greater 两 array

        for elem in arr[1:]:                    #3. 除 pivot 之外，其它放入 less & greater 两个 list
            if elem < pivot:
                less.append(elem)
            else:
                greater.append(elem)

        return self.quickSort(less) + [pivot] + self.quickSort(greater)     #4. return [less]+[pivot]+[greater]

sol = Solution()

arr = [5, 2, 7, 6, 1, 9, 8]

#res = sol.bubbleSort(arr)
res = sol.quickSort(arr)
#res = sol.quick_sort(arr)
print(f"res = {res}")