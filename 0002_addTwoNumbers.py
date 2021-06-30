# Definition for singly-linked list.
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = cur = ListNode()
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            cur.next = ListNode(carry % 10)
            cur = cur.next
            carry //= 10
        return dummy.next


def lst2link(lst):
    dummy = cur = ListNode()
    for e in lst:
        cur.next = ListNode(e)
        cur = cur.next
    return dummy.next


l1 = [2, 4, 9]
l2 = [5, 6, 4]
sol = Solution()
current = sol.addTwoNumbers(lst2link(l1), lst2link(l2))
while current is not None:
    print(current.val)
    current = current.next
