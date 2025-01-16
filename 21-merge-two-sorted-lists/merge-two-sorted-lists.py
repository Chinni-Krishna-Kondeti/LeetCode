# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        output = list1
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1.val > list2.val:
            list1, list2 = list2, list1
        output = list1
        old_node = None
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                old_node = list1
                list1 = list1.next
            else:
                temp = list2.next
                old_node.next = list2
                old_node = list2
                list2.next = list1
                list2 = temp
        if list2 is not None:
            old_node.next = list2
        return output