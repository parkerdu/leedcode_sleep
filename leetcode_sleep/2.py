# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):

        root = l = ListNode(0)

        carry = 0
        while carry or l2 or l1:
            if l1 and l2:
                val = l1.val+l2.val+carry
            elif l1 and not l2:
                val = l1.val + carry
            elif not l1 and l2:

                val = l2.val + carry
            else:
                val = 1
            if val >= 10:
                l.next = ListNode(val%10)
                carry = 1
            else:
                l.next = ListNode(val)
                carry = 0
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            l = l.next
        return root.next

    def addTwoNumbers(self, l1, l2):
        """优化版本，你要学会用下面的方法，来缩减讨论所有情况
            本来讨论起来确实是上面代码的四种情况
            但是这四种无非就是加一个l1.val还是加一个l2.val
            用两个并列的if就可以解决"""

        root = l = ListNode(0)
        carry = 0
        while carry or l2 or l1:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            l.next = ListNode(carry%10)
            carry //= 10
            l = l.next
        return root.next

if __name__ == "__main__":
    # 链表的构造比二叉树简单多了，不要想多了，下面即为构造出的链表

    l1 = root1 = ListNode(0)
    root1.next = ListNode(0)
    root1.next = ListNode(5)

    l2 = root2 = ListNode(0)
    root2.next = ListNode(0)
    root2.next = ListNode(5)

    su = Solution()
    su.addTwoNumbers(l1,l2)



