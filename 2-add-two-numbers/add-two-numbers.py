# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        output = l1
        carry = 0
        value = 0
        last_node = l1
        while l1 is not None or l2 is not None:
            if l1 is not None:
                value += l1.val
            if l2 is not None:
                value += l2.val
            value += carry
            carry = 0
            if l1 is None:
                last_node.next = l2
                l1 = last_node.next
                l2 = None
            if value < 10:
                l1.val = value
            else:
                l1.val = value - 10
                carry = 1
            last_node = l1
            l1 = l1.next
            if l2 is not None: l2 = l2.next
            value = 0
        if carry == 1:
            new_node = ListNode()
            new_node.val = 1
            last_node.next = new_node
        return output