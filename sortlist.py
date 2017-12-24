# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        if l1.val < l2.val:
            prev=l1
            cur = l1.next
            bottom = l2
            head = l1
        else:
            prev=l2
            cur=l2.next
            bottom=l1
            head=l2

        while cur is not None and bottom is not None:
            if cur.val < bottom.val:
                prev = cur
                cur = cur.next
            else:
                node = bottom
                bottom = bottom.next
                node.next= None
                prev.next = node
                node.next=cur
                prev=node

        if bottom is not None:
            prev.next = bottom

        return head
    def merge_sorted_list(self, list1, list2):
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        newlist = ListNode(list1.val)
        head = newlist
        if list1.val > list2.val:
            newlist = ListNode(list2.val)
            head = newlist
            list2 = list2.next
        else:
            list1 = list1.next
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                newlist.next = ListNode(list1.val)
                newlist = newlist.next
                list1 = list1.next
            else:
                newlist.next = ListNode(list2.val)
                newlist = newlist.next
                list2 = list2.next

        while list1 is not None:
            newlist.next = ListNode(list1.val)
            newlist = newlist.next
            list1 = list1.next

        while list2 is not None:
            newlist.next = ListNode(list2.val)
            newlist = newlist.next
            list2 = list2.next

        return head

    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # return merge_sorted_list(list1, list2)

        def get_halves(lst):
            if lst is None or lst.next is None:
                return lst, None
            elif lst.next.next is None:
                nxt = lst.next
                lst.next = None
                return lst, nxt
            slow = lst
            fast = lst
            while fast is not None and fast.next is not None:
                slow = slow.next
                fast = fast.next.next
            nxt = slow.next
            slow.next = None
            return lst, nxt

        def merge_sort(lst):
            if lst is None or lst.next is None:
                return lst
            # print_list(lst)
            first, second = get_halves(lst)
            # print_list(first)
            # print_list(second)
            # print()
            left = merge_sort(first)
            right = merge_sort(second)
            sorted_lst = self.mergeTwoLists(left, right)
            return sorted_lst

        # return get_halves(head)

        return merge_sort(head)


from extras import *

l1 = create_random_list(20, sort_flag=True)
l2 = create_random_list(1, sort_flag=True)
# print_list(l1)
# print_list(l2)

l = create_random_list(10)
print_list(l)
s=Solution()
l3 = s.sortList(l)
# l3 = s.merge_sorted_list(l1, l2)
print_list(l3)
# print_list(l4)