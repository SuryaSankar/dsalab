# https://leetcode.com/problems/merge-in-between-linked-lists/description/


from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        left_link = list1
        for i in range(1, a):
            left_link = left_link.next
        right_link = left_link # a-1 node
        for _ in range(a, b+1):
            right_link = right_link.next
        list2_iter = list2
        while list2_iter.next is not None:
            list2_iter = list2_iter.next
        left_link.next = list2
        list2_iter.next = right_link.next
        return list1