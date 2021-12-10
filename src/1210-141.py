'''
Created on Dec 10, 2021

1. 用快慢指针的方法，fast每次走2步，slow每次走1步
   - if fast == slow: return True
   - if fast == None or slow == None: return False

@author: mayijie
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        (fast, slow) = (head, head)
        if head == None or head.next == None: return False
        if head.next == head: return True
        fast = fast.next.next
        slow = slow.next
        while not (fast == slow or fast == None or fast.next == None or slow == None):
            fast = fast.next.next
            slow = slow.next
        if fast == None or fast.next == None or slow == None: return False
        else: return True


if __name__ == "__main__":
    sol = Solution()

    a4 = ListNode(-4)
    a3 = ListNode(0)
    a2 = ListNode(2)
    a1 = ListNode(3)
    a1 = None

    a4.next = a2
    a3.next = a4
    a2.next = a1
    #a1.next = None
    
    res = sol.hasCycle(a1)
    print (res)