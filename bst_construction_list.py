# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


from extras import *
from graph import *

def mid_node(cur):
	if cur is None:
		return None
	if cur.next is None:
		return cur
	slow = cur
	fast = cur.next.next
	while fast is not None and fast.next is not None:
		slow = slow.next 
		fast = fast.next.next
	return slow
class Solution:
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if head is None:
        	return None
        elif head.next is None:
        	return TreeNode(head.val)
        elif head.next.next is None:
        	cur = TreeNode(head.val)
        	cur.right = TreeNode(head.next.val)
        	return cur
        else:
        	mid = mid_node(head)
        	cur_val = mid.next
        	right = cur_val.next
        	mid.next = None
        	# print_list(mid_next)
        	cur = TreeNode(cur_val.val)
        	cur.left = self.sortedListToBST(head)
        	cur.right = self.sortedListToBST(right)
        	return cur



a=[1,2,3,4]
s=Solution()
l = list_to_linkedlist(a)
# print_list(l)
# mid = mid_node(l)
# mid_next = mid.next 
# mid.next = None
# print_list(l)
# print_list(mid_next)
t = s.sortedListToBST(l)
print(inorder(t))