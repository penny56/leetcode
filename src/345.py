class Solution:
    def reverseVowels(self, s: str) -> str:
        list1 = ['a','A','e','E','o','O','u','U','i','I']
        new=[]
        for i in s:
            if i in list1:
                new.append(i)

        new=new[::-1]
        j=0
        s1 = list(s)
        for i in range(len(s1)):
            if s1[i] in list1:
                s1[i] = new[j]
                j+=1
        return ''.join(s1)
