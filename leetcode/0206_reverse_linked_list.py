# LeetCode 206. Reverse Linked List
#
# Given the head of a singly linked list, reverse the list, and return the reversed list.
#
# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
#
# Example 2:
# Input: head = [1,2]
# Output: [2,1]
#
# Example 3:
# Input: head = []
# Output: []
#
# Constraints:
# - The number of nodes in the list is the range [0, 5000].
# - -5000 <= Node.val <= 5000
#
# Follow up:
# A linked list can be reversed either iteratively or recursively.
# Could you implement both?




# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
     
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
  
        return prev


# Test
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

result = Solution().reverseList(head)

while result:
    print(result.val, end=" ")
    result = result.next
# Expected output: 5 4 3 2 1