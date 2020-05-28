"""
876. Middle of the Linked List

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        
        slow = head
        fast = head
        
        if head == None:
            return -1
        
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            
            
        return slow