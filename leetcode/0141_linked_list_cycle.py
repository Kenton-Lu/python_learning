# LeetCode 141. Linked List Cycle
#
# Given head, the head of a linked list, determine if the linked list has a cycle in it.
#
# There is a cycle in a linked list if there is some node in the list that can be reached again
# by continuously following the next pointer.
#
# Return true if there is a cycle in the linked list. Otherwise, return false.
#
# Example 1:
# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
#
# Example 2:
# Input: head = [1,2], pos = 0
# Output: true
#
# Example 3:
# Input: head = [1], pos = -1
# Output: false


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False

# Test 1: cycle
head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(0)
head.next.next.next = ListNode(-4)

# create cycle: -4 -> 2
head.next.next.next.next = head.next

print(Solution().hasCycle(head))  # Expected: True


# Test 2: no cycle
head2 = ListNode(1)
head2.next = ListNode(2)

print(Solution().hasCycle(head2))  # Expected: False