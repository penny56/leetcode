class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """

        arrOri = path.split('/')
        arrNew = []

        while len(arrOri) != 0:
            curr = arrOri.pop(0)

            if curr == '': continue

            if curr == '.': continue

            if curr == '..':
                if arrNew: arrNew.pop(-1)
                continue
            arrNew.append(curr)

        str = "/"
        while len(arrNew) != 0:
            str += arrNew.pop(0)
            str += "/"
        
        if len(str) != 1: str = str[:-1]
        return str
        

sol = Solution()

path = "/home/"

res = sol.simplifyPath(path)
print ("res = ", res)





