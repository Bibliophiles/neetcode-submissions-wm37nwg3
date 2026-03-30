# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        first_pointer, second_pointer = dummy, dummy

        for _ in range(n):
            second_pointer = second_pointer.next

        while second_pointer.next != None:
            first_pointer = first_pointer.next
            second_pointer = second_pointer.next

        first_pointer.next = first_pointer.next.next

        return dummy.next
