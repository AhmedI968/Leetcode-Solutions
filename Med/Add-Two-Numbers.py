# Solution to the Add Two Numbers problem
# Problem link: https://leetcode.com/problems/add-two-numbers/description/
# Given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contains a single digit. Add the two numbers and return it as a linked list.
# What I did was to create a dummy node to keep track of the head of the new linked list.
# Then, I iterate through both linked lists, adding the corresponding digits along with any carry from the previous addition.
# If the sum of the two digits is greater than 9, I set carry to 1 for the next iteration.
# Otherwise, I set carry to 0.
# I create a new node with the value of the sum modulo 10 and set it as the next node of the current node.
# I then move the current node to the new node.
# After processing both linked lists, if there is still a carry, I create a new node with the value of carry.
# Finally, I return the next node of the dummy node, which is the head of the new linked list.
# The time complexity of this solution is O(max(m, n)), where m and n are the lengths of the two linked lists.
# The space complexity is O(max(m, n)) as well, since we are creating a new linked list to store the result.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total%10)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next