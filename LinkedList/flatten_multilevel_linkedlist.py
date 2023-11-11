# leetcode 430. Flatten a Multilevel Doubly Linked List

# You are given a doubly linked list, which contains nodes that have a next pointer, a previous pointer, and an additional child pointer. This child pointer may or may not point to a separate doubly linked list, also containing these special nodes. These child lists may have one or more children of their own, and so on, to produce a multilevel data structure as shown in the example below.
# Given the head of the first level of the list, flatten the list so that all the nodes appear in a single-level, doubly linked list. Let curr be a node with a child list. The nodes in the child list should appear after curr and before curr.next in the flattened list.
# Return the head of the flattened list. The nodes in the list must have all of their child pointers set to null.

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Solution:
    def flatten(self, head: "Optional[Node]") -> "Optional[Node]":
        # recursively put all of the children on the same level as the parent between parent and next Node
        if not head:
            return head
        start = Node(None, None, head, None)
        self.flatten_dfs(start, head)
        # detatch head from start node that we made.
        start.next.prev = None
        return start.next

    def flatten_dfs(self, prev, curr):
        if not curr:
            return prev
        curr.prev = prev
        prev.next = curr

        tempNext = curr.next
        # run the function to recursively bring the children up a level
        tail = self.flatten_dfs(curr, curr.child)
        curr.child = None
        # finally, process the remaining data
        return self.flatten_dfs(tail, tempNext)
