# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        h1 = l1
        (value, flag) = (0, 0)
        while l1 and l2:
            value = l1.val + l2.val + flag
            
            if value > 9:
                value = value%10
                flag = 1
            else:
                flag = 0
            l1.val = value 
            if l1.next == None:
                l1.next = l2.next
                break
            if l2.next == None:
                break
            l1 = l1.next
            l2 = l2.next
        if flag == 1:
            if l1.next == None:
                n = ListNode()
                l1.next = n
                n.val = flag
            else:
                while l1:
                    l1.val += 1
                    if l1.val > 9:
                        flag = 1
                        l1.val = 0
                        if l1.next != None:
                            l1 = l1.next
                        else:
                            n = ListNode()
                            l1.next = n
                            n.val = 1
                            break
                    else:
                        break
        return h1


sol = Solution()

n17 = ListNode(9)
n16 = ListNode(9, n17)
n15 = ListNode(9, n16)
n14 = ListNode(9, n15)
n13 = ListNode(9, n14)
n12 = ListNode(9, n13)
n11 = ListNode(9, n12)
l1 = n11

n24 = ListNode(9)
n23 = ListNode(9, n24)
n22 = ListNode(9, n23)
n21 = ListNode(9, n22)
l2 = n21

res = sol.addTwoNumbers(l1, l2)
while res.next != None:
    print (res.val)
    res = res.next
print (res.val)