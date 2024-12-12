class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        
        (arr1, arr2) = (list(num1), list(num2))
        (value1, value2) = (0, 0)
        print(f"arr1 = {arr1}")

        for i in range(len(arr1)):
            j = len(arr1)-1-i
            value1 = value1 + int(arr1[i]) * 10 ** j

        for i in range(len(arr2)):
            j = len(arr2)-1-i
            value2 = value2 + int(arr2[i]) * 10 ** j

        value = value1 * value2
            
        return value


sol = Solution()
num1 = "123"
num2 = "456"

res = sol.multiply(num1, num2)
print ("res = ", res)





