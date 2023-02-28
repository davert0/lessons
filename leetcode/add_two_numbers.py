from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        l1_vals = []
        l2_vals = []
        while l1.next:
            l1_vals.append(str(l1.val))
            l1 = l1.next
        l1_vals.append(str(l1.val))
        while l2.next:
            l2_vals.append(str(l2.val))
            l2 = l2.next
        l2_vals.append(str(l2.val))
        sum = str(
            int("".join(reversed(l1_vals)) if l1_vals else 0)
            + int("".join(reversed(l2_vals)) if l2_vals else 0)
        )
        node = ListNode(sum[0])
        for i in range(1, len(sum)):
            node = ListNode(sum[i], node)
        return node
