# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    @staticmethod
    def mergeTwoLists(list1, list2):
        if list1 == None or list2 == None:
            return list1 if list1 else list2
        head = list1 if list1.val <= list2.val else list2
        prev = None
        prev2 = None
        while list1 and list2:
            if list1.val <= list2.val:
                temp = list1.next
                list1.next = list2
                list2 = list2.next
                list1.next.next = temp
                prev2 = list1.next
                list1 = list1.next
            else:
                if prev:
                    temp = list2
                    prev.next = temp
                    temp.next = list1
                    prev2 = list2
                    list2 = list2.next
                else:
                    # head = list2
                    # temp = list2
                    # temp.next = list1
                    prev2 = list2
                    list2 = list2.next
                    # list1 = list1.next
        if prev2 and list1:
            prev2.next = list1
        elif prev2 and list2:
            prev2.next = list2
        return head

listt1 = ListNode(-9)
listt1.next = ListNode(3)
# listt1.next.next = ListNode(4)
listt2 = ListNode(5)
listt2.next = ListNode(7)
# listt2.next.next = ListNode(4)
Solution.mergeTwoLists(listt1, listt2)