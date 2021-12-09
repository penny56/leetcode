'''
Created on Dec 9, 2021

1. 

@author: mayijie
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head.next == None: return None
        (f1, f2, cnt) = (head, head, 0)
        while f1.next != None:
            f1 = f1.next
            if cnt >= n: f2 = f2.next
            cnt += 1
        if cnt < n:
            # the f2 didn't moved once, remove the head
            head = head.next
        else:
            f2.next = f2.next.next
        return head

if __name__ == "__main__":
    sol = Solution()

    a5 = ListNode(5)
    a4 = ListNode(4, a5)
    a3 = ListNode(3, a4)
    a2 = ListNode(2, a3)
    a1 = ListNode(1, a2)

    res = sol.removeNthFromEnd(a1, 2)
    print (res)