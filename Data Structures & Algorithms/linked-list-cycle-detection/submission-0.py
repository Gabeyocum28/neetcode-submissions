# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        while head and head.val != -1:
            prev = head
            head = head.next
            prev.val = -1
        if head is None:
            return False
        return True